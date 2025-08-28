"""
Zhesp2 wrapper for fsociety obfuscation module
"""

import os
from pathlib import Path

from fsociety.core.repo import GitHubRepo


class Zhesp2Repo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="CEO-netizen/zhesp2",
            install=None,
            description="File and text encryption tool using ZHESP2 protocol",
        )

    def run(self):
        os.chdir(self.full_path)
        print("Launching Zhesp2 interactive terminal...")
        return os.system("python3 -m zhesp2")


zhesp2 = Zhesp2Repo()
