# Core
from fsociety.core.menu import tools_cli

from .cupp import cupp
from .cr3dov3r import cr3dov3r
from .hash_buster import hash_buster

__tools__ = {
    "cupp": cupp,
    "cr3dov3r": cr3dov3r,
    "hash_buster": hash_buster
}


def cli():
    tools_cli(__name__, __tools__)
