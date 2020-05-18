import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.usernames import get_usernames, add_username


class cr3dov3rRepo(GitHubRepo):
    def __init__(self, path="D4Vinci/Cr3dOv3r", install={"pip": "requirements.txt"}):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_email = input("\nEnter a email: ").strip()
        return os.system(f"python3 Cr3d0v3r.py {user_email}")


cr3dov3r = cr3dov3rRepo()
