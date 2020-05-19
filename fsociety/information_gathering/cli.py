# Core
from fsociety.core.menu import tools_cli

from .host2ip import host2ip
from .nmap import nmap
from .sqlmap import sqlmap
from .sublist3r import sublist3r
from .sherlock import sherlock
from .s3scanner import s3scanner

__tools__ = {
    "host2ip": host2ip,
    "nmap": nmap,
    "sqlmap": sqlmap,
    "sublist3r": sublist3r,
    "sherlock": sherlock,
    "s3scanner": s3scanner
}


def cli():
    tools_cli(__name__, __tools__)
