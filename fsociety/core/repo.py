import os
from abc import ABCMeta, abstractmethod
from shutil import rmtree, which
from typing import Dict, Iterable, List, Optional, Union

from git import RemoteProgress, Repo
from rich.progress import BarColumn, Progress, TaskID
from rich.table import Table

from fsociety.console import console
from fsociety.core.config import INSTALL_DIR, get_config
from fsociety.core.menu import confirm

config = get_config()


def print_pip_deps(packages: Union[str, Iterable[str]]) -> None:
    requirements = []
    if isinstance(packages, str) and os.path.exists(packages):
        with open(packages, encoding="utf-8") as requirements_file:
            for line in requirements_file:
                if line.strip():
                    requirements.append(line)
    elif isinstance(packages, Iterable):
        requirements = list(packages)
    else:
        raise ValueError
    table = Table("Packages", title="Pip Dependencies")
    for req in requirements:
        table.add_row(req)
    console.print()
    console.print(table)


class InstallError(Exception):
    pass


class CloneError(Exception):
    pass


class GitProgress(RemoteProgress):
    def __init__(self) -> None:
        super().__init__()
        self.progress = Progress(
            "[progress.description]{task.description}",
            BarColumn(None),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "[progress.filesize]{task.fields[msg]}",
        )
        self.current_opcode = None
        self.task: Optional[TaskID] = None

    def update(
        self, opcode, count: int, max_value: int, msg: Optional[str] = None
    ) -> None:
        opcode_strs = {
            self.COUNTING: "Counting",
            self.COMPRESSING: "Compressing",
            self.WRITING: "Writing",
            self.RECEIVING: "Receiving",
            self.RESOLVING: "Resolving",
            self.FINDING_SOURCES: "Finding sources",
            self.CHECKING_OUT: "Checking out",
        }
        stage, real_opcode = opcode & self.STAGE_MASK, opcode & self.OP_MASK

        try:
            count = int(count)
            max_value = int(max_value)
        except ValueError:
            return

        if self.current_opcode != real_opcode:
            if self.task:
                self.progress.update(self.task, total=1, completed=1, msg="")
            self.current_opcode = real_opcode
            self.task = self.progress.add_task(
                opcode_strs[real_opcode].ljust(15), msg=""
            )

        if stage & self.BEGIN:
            self.progress.start()
        if stage & self.END:
            self.progress.stop()
        if self.task:
            self.progress.update(
                self.task, msg=msg or "", total=max_value, completed=count
            )


class GitHubRepo(metaclass=ABCMeta):
    def __init__(
        self,
        path: str = "fsociety-team/fsociety",
        install: Union[str, Dict[str, Union[str, List[str]]]] = "pip install -e .",
        description=None,
    ) -> None:
        self.path = path
        self.name = self.path.split("/")[-1]
        self.install_options = install
        self.full_path = os.path.join(INSTALL_DIR, self.name)
        self.description = description
        self.scriptable_os = ["debian", "windows", "macos", "arch"]

    def __str__(self) -> str:
        return self.name.lower().replace("-", "_")

    def clone(self, overwrite: bool = False) -> str:
        if os.path.exists(self.full_path):
            if not overwrite:
                repo = Repo(self.full_path)
                repo.remotes.origin.pull()
                return self.full_path
            rmtree(self.full_path)
        url = f"https://github.com/{self.path}"
        if config.getboolean("fsociety", "ssh_clone"):
            url = f"git@github.com:{self.path}.git"
        Repo.clone_from(url, self.full_path, progress=GitProgress())
        if not os.path.exists(self.full_path):
            raise CloneError(f"{self.full_path} not found")
        return self.full_path

    def install(self, no_confirm: bool = False, clone: bool = True) -> None:
        if no_confirm or not confirm(
            f"\nDo you want to install https://github.com/{self.path}?"
        ):
            print("Cancelled")
            return
        command = "exit 1"  # avoid unset issues
        if clone:
            self.clone()
        if self.install_options:
            if clone:
                os.chdir(self.full_path)
            else:
                os.chdir(INSTALL_DIR)
            install = self.install_options
            target_os = config.get("fsociety", "os")

            if isinstance(install, dict):
                if "pip" in install:
                    packages = install.get("pip")
                    message = ""  # avoid unset issues
                    if isinstance(packages, list):
                        message = "Do you want to install these packages?"
                        packages_str = " ".join(packages)
                        command = f"pip install {packages_str}"
                    elif isinstance(packages, str):
                        requirements_txt = os.path.join(
                            self.full_path, "requirements.txt"
                        )
                        message = f"Do you want to install these packages from {requirements_txt}?"
                        command = f"pip install -r {requirements_txt}"

                    if packages:
                        print_pip_deps(packages)
                    if not confirm(message):
                        raise InstallError("User Cancelled")

                elif "go" in install and which("go"):
                    command = install.get("go")

                elif "binary" in install:
                    bin_url = install.get("binary")
                    if which("curl"):
                        command = (
                            f"curl -L -o {self.full_path}/{self.name} -s {bin_url}"
                        )
                    elif which("wget"):
                        command = f"wget -q -O {self.full_path}/{self.name} {bin_url}"
                    else:
                        raise InstallError("Supported download tools missing")
                    command = f"mkdir {self.full_path} && {command} && chmod +x {self.full_path}/{self.name}"
                elif target_os == "macos" and "brew" in install and which("brew"):
                    brew_opts = install.get("brew")
                    command = f"brew {brew_opts}"
                elif target_os in install and target_os in self.scriptable_os:
                    command = str(install[target_os])
                else:
                    raise InstallError(
                        f"Platform not supported, missing {', '.join(install.keys())}"
                    )
            else:
                command = install

            os.system(command)

    def installed(self) -> bool:
        return os.path.exists(self.full_path)

    @abstractmethod
    def run(self) -> int:
        pass
