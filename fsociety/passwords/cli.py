# Core
from fsociety.core.menu import tools_cli

from .changeme import changeme
from .cr3dov3r import cr3dov3r
from .cupp import cupp
from .hash_buster import hash_buster
from .traitor import traitor

__tools__ = [cupp, cr3dov3r, hash_buster, changeme, traitor]


def cli():
    tools_cli(__name__, __tools__)
