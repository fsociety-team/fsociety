from abc import ABCMeta, abstractmethod
import os

from fsociety.core.config import install_dir, get_config

config = get_config()


class CloneError(Exception):
    pass


class GitHubRepo(metaclass=ABCMeta):
    def __init__(self, path="fsociety-team/fsociety", install="pip install -e .", default_os="default"):
        self.path = path
        self.install_command = install
        if isinstance(install, dict):
            self.install_command = install.get(config.get(
                "fsociety", "os"), install.get(default_os))
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
            url = f"https://github.com/{self.path}"
        os.system(f"git clone {url} {self.full_path}")
        return self.full_path

    def install(self):
        self.clone()
        if not os.path.exists(self.full_path):
            raise CloneError(f"{self.full_path} not found")
        os.chdir(self.full_path)
        if self.install_command:
            os.system(self.install_command)

    @abstractmethod
    def run(self):
        pass
