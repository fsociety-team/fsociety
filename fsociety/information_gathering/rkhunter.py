import os

from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo
from fsociety.core.usernames import add_username, get_usernames


class rkhunter(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="youngunix/rkhunter",
            install=None,
            description="a tool that scans for rootkits, backdoors.",
        )

    def run(self):
        os.chdir(self.full_path)
        command = input("Choose either [check, unlock, update, versioncheck] ")

        return os.system(f"sudo rkhunter --{command}")