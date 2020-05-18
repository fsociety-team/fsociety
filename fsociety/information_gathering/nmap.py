import os
from shutil import which

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.hosts import get_hosts, add_host, InvalidHost

premade_args = {
    "simple": "{host}",
    "common_ports": "-F {host}",
    "all_ports": "-p- {host}",
    "detect_os": "-A {host}",
    "tcp_syn_scan": "-sS {host}",
    "tcp_connect": "-sT {host}",
    "nse_standard": "-sV -sC {host}",
    "detect_web_app": "--script=http-enum {host}",
    "heartbleed_test": "-sV -p 443 --script=ssl-heartbleed {host}",
}


class nmapRepo(GitHubRepo):
    def __init__(self, path="nmap/nmap", install="./configure && make && make install"):
        super().__init__(path=path, install=install)

    def installed(self):
        return which("nmap")

    def run(self):
        hosts = get_hosts()
        set_readline(hosts)
        host = input("\nEnter a host: ").strip()
        if not host:
            raise InvalidHost
        if (host not in hosts):
            add_host(host)
        longest_key = max([len(key) for key in premade_args.keys()]) + 2
        print("\nName".ljust(longest_key) + " | Args")
        for name, args in premade_args.items():
            print(f"{name.ljust(longest_key)}: {args.format(host=host)}")
        set_readline(premade_args.keys())
        selected = input("\nMake a selection: ")
        if selected and selected in premade_args.keys():
            args = premade_args.get(selected).format(host=host)
            return os.system(f"nmap {args}")
        return self.run()


nmap = nmapRepo()
