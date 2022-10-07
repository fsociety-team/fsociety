import os
from shutil import which

from fsociety.core.hosts import InvalidHost, add_host, get_hosts
from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo

premade_args = {
    "simple": "{host}",
    "common_ports": "-F {host}",
    "all_ports": "-p- {host}",
    "detect_os": "-A {host}",
    "tcp_syn_scan": "-sS {host}",
    "tcp_connect": "-sT {host}",
    "nse_standard": "-sV -sC {host}",
    "vuln_scan": "-Pn --script vuln {host}",
    "google_malware": "-p80 --script http-google-malware {host}",
    "aggressive_scan": "-A -T4 {host}",
    "detect_web_app": "--script=http-enum {host}",
    "subdomain_enumeration": "-sn --script hostmap-crtsh {host}",
    "heartbleed_test": "-sV -p 443 --script=ssl-heartbleed {host}",
    "slowloris": "-max-parallelism 800 -Pn --script http-slowloris --script-args http-slowloris.runforever=true {host}",
}


class NmapRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="nmap/nmap",
            install={
                "arch": "sudo pacman -Sy nmap",
                "brew": "install nmap",
                "linux": "sudo apt-get install nmap",
            },
            description="the Network Mapper",
        )

    def installed(self):
        return which("nmap")

    def install(self):
        super().install(clone=False)

    def run(self):
        hosts = get_hosts()
        set_readline(hosts)
        host = input("\nEnter a host: ").strip()
        if not host:
            raise InvalidHost
        if host not in hosts:
            add_host(host)
        longest_key = max(len(key) for key in premade_args) + 2
        print("\nName".ljust(longest_key) + " | Args")
        for name, args in premade_args.items():
            print(f"{name.ljust(longest_key)}: {args.format(host=host)}")
        set_readline(premade_args.keys())
        selected = input("\nMake a selection: ")
        if selected and selected in premade_args:
            args = premade_args.get(selected).format(host=host)
            return os.system(f"nmap {args}")
        return self.run()


nmap = NmapRepo()
