import os
from abc import ABCMeta, abstractmethod

from fsociety.core.config import install_dir, get_config
from fsociety.core.menu import confirm

config = get_config()


class InstallError(Exception):
    pass


class CloneError(Exception):
    pass


class GitHubRepo(metaclass=ABCMeta):
    def __init__(self, path="fsociety-team/fsociety", install="pip install -e ."):
        self.path = path
        self.install_options = install
        self.full_path = os.path.join(install_dir, self.path.split("/")[-1])

    def __str__(self):
        return self.path

    def clone(self):
        if os.path.exists(self.full_path):
            os.chdir(self.full_path)
            os.system(f"git pull")
            return self.full_path
        url = f"https://github.com/{self.path}"
        if config.getboolean("fsociety", "ssh_clone"):
            url = f"git@github.com:{self.path}.git"
        os.system(f"git clone {url} {self.full_path}")
        if not os.path.exists(self.full_path):
            raise CloneError(f"{self.full_path} not found")
        return self.full_path

    def install(self, no_confirm=False):
        if no_confirm or not confirm(f"\nDo you want to install https://github.com/{self.path}?"):
            print("Cancelled")
            return
        self.clone()
        if self.install_options:
            os.chdir(self.full_path)
            install = self.install_options

            if isinstance(install, dict):
                if "pip" in install.keys():
                    packages = install.get("pip")
                    if isinstance(packages, list):
                        message = f"Do you want to install the following packages? {packages}"
                        packages_str = " ".join(packages)
                        command = f"pip install {packages_str}"
                    elif isinstance(packages, str):
                        requirements_txt = os.path.join(
                            self.full_path, "requirements.txt")
                        message = f"Do you want to install the packages in {requirements_txt}?"
                        command = f"pip install -r {requirements_txt}"

                    if not confirm(message):
                        raise InstallError

                elif "linux" in install.keys() or "windows" in install.keys() or "macos" in install.keys():
                    command = install.get(config.get(
                        "fsociety", "os"), install.get("linux"))
            else:
                command = install

            print()
            os.system(command)

    def installed(self):
        return os.path.exists(self.full_path)

    @abstractmethod
    def run(self):
        pass
