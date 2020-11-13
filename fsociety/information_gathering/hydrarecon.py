import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline, confirm
from fsociety.core.config import INSTALL_DIR


class HydrareconRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="aufzayed/HydraRecon",
            install={"pip": "requirements.txt"},
            description="Simple recon tool",
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domain = input("\nEnter a domain to scan: ").strip()
        arg = "--basic"
        if confirm("\nDo you want to crawl? [default=No]"):
            arg = "--crawl"
        return os.system(
            f"python3 hydrarecon.py -d {user_domain} -o {INSTALL_DIR} {arg}"
        )


hydrarecon = HydrareconRepo()
