import os

from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo


class Cr3dov3rRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="D4Vinci/Cr3dOv3r",
            install={"pip": "requirements.txt"},
            description="Your best friend in credential reuse attacks",
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_email = input("\nEnter a email: ").strip()
        return os.system(f"python3 Cr3d0v3r.py {user_email}")


cr3dov3r = Cr3dov3rRepo()
