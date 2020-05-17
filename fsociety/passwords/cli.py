# Core
from fsociety.menu import set_readline

__tools__ = ["tool1", "tool2", "tool3"]


def menutools():
    return "".join(["\n\t" + tool for tool in __tools__])


def cli():
    print("Passwords!")
    print(menutools())
    set_readline(__tools__)
    selected_tool = input("Select a tool: ")
    print(selected_tool)
