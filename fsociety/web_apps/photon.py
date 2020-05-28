import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import confirm


class photonRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="s0md3v/Photon",
                         install={"pip": "requirements.txt"},
                         description="Incredibly fast crawler designed for OSINT")

    def run(self):
        os.chdir(self.full_path)
        user_url = input("\nEnter a url to scan: ").strip()
        args = list()
        if confirm("Do you want to clone the site?"):
            args.append("--clone")
        if confirm("Do you want to use wayback?"):
            args.append("--wayback")
        args_str = " ".join(args)
        return os.system(f"python3 photon.py --url {user_url} {args_str}")


photon = photonRepo()
