import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import confirm


class xsstrikeRepo(GitHubRepo):
    def __init__(self, path="s0md3v/XSStrike", install={"pip": "requirements.txt"}):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        user_url = input("\nEnter a url to scan: ").strip()
        args = list()
        if confirm("Do you want to crawl?"):
            args.append("--crawl")
        if confirm("Do you want to find hidden parameters?"):
            args.append("--params")
        args_str = " ".join(args)
        return os.system(f"python3 xsstrike.py --url {user_url} {args_str}")


xsstrike = xsstrikeRepo()
