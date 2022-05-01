# Core
from fsociety.core.menu import tools_cli

from .gitgraber import gitgraber
from .hydrarecon import hydrarecon
from .s3scanner import s3scanner
from .sherlock import sherlock
from .sqlmap import sqlmap
from .striker import striker
from .sublist3r import sublist3r

__tools__ = [sqlmap, striker, sublist3r, sherlock, s3scanner, gitgraber, hydrarecon]


def cli():
    tools_cli(__name__, __tools__)
