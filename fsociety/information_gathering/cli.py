# Core
from fsociety.core.menu import tools_cli

from .nmap import nmap
from .sublist3r import sublist3r
from .sherlock import sherlock
from .s3scanner import s3scanner

__tools__ = {
    "nmap": nmap,
    "sublist3r": sublist3r,
    "sherlock": sherlock,
    "s3scanner": s3scanner
}


def cli():
    tools_cli(__name__, __tools__)
