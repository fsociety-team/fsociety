import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.usernames import get_usernames, add_username


class sublist3rRepo(GitHubRepo):
    def __init__(self, path="aboul3la/Sublist3r", install={"pip": "requirements.txt"}):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domain = input("\nEnter a domain to enumerate: ").strip()
        return os.system(f"python3 sublist3r.py -v -d {user_domain}")


sublist3r = sublist3rRepo()
