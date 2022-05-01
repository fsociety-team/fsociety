import os
from shutil import which

from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo

premade_args = {"any": "-a"}
arch_map = {"x86_64": "amd64", "i386": "386"}


class TraitorRepo(GitHubRepo):
    def __init__(self):
        if os.uname().machine in arch_map.keys():
            self.arch = arch_map.get(os.uname().machine)
        else:
            self.arch = ""
        self.version = "v0.0.14"
        super().__init__(
            path="liamg/traitor",
            install={"binary": ""},
            description="Automatic Linux privesc via exploitation of low-hanging fruit",
        )

    def installed(self):
        return which(f"{self.full_path}/{self.name}")

    def install(self, no_confirm: bool = False, clone: bool = False):
        artifact = f"https.*/traitor-{self.arch}"
        url = "https://api.github.com/repos/liamg/traitor/releases/latest"
        if which("curl"):
            command = f"curl -s {url} | grep -wo '{artifact}'"
        elif which("wget"):
            command = f"wget -qO - {url} | grep -wo '{artifact}'"

        self.install_options["binary"] = os.popen(command).read().strip("\n")
        return super().install(no_confirm, clone)

    def run(self) -> int:
        longest_key = max(len(key) for key in premade_args) + 2
        print("\nName".ljust(longest_key) + " | Args")
        for name, args in premade_args.items():
            print(f"{name.ljust(longest_key)}: {args.format()}")
        set_readline(premade_args.keys())
        selected = input("\nMake a selection: ")
        if selected and selected in premade_args:
            return os.system(
                f"{self.full_path}/{self.name} {premade_args.get(selected)}"
            )
        elif (
            selected and selected not in premade_args.keys()
        ):  # allow passing custom specific exploits
            return os.system(f"{self.full_path}/{self.name} -e {selected}")
        return self.run()


traitor = TraitorRepo()
