import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline


class strikerRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="s0md3v/Striker",
                         install={"pip": "requirements.txt"},
                         description="Recon & Vulnerability Scanning Suite")

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domain = input("\nEnter a domain to scan: ").strip()
        return os.system(f"python3 striker.py {user_domain}")


striker = strikerRepo()
