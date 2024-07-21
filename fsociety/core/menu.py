import os
from typing import Iterable

from rich import box
from rich.style import Style
from rich.table import Table
from rich.text import Text

from fsociety.console import console
from fsociety.core.config import INSTALL_DIR

BACK_COMMANDS = ["back", "return"]


class CommandCompleter:
    def __init__(self, options: Iterable[str]):
        self.options = sorted(options)

    def complete(self, text: str, state: int):
        response = None
        matches = []
        if state == 0:
            if text:
                matches = [s for s in self.options if s and s.startswith(text.lower())]
            else:
                matches = self.options[:]
        try:
            response = matches[state]
        except IndexError:
            pass
        return response


def set_readline(items: Iterable[str]):
    try:
        import readline
    except ImportError:
        pass
    else:
        import rlcompleter  # noqa: F401

        if isinstance(items, list):
            readline.set_completer(CommandCompleter(items).complete)
        elif isinstance(items, dict):
            readline.set_completer(CommandCompleter(items.keys()).complete)
        else:
            readline.set_completer(CommandCompleter(list(items)).complete)
        readline.parse_and_bind("tab: complete")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_tools(tools):
    cutoff = 5
    etc = False
    if len(tools) > cutoff:
        tools = tools[:cutoff]
        etc = True
    res = "".join([f"\n{str(tool)}" for tool in tools])
    if etc:
        res += "\n..."
    return res


def module_name(module):
    return module.__name__.split(".")[-1]


def prompt(path="", base_path="~"):
    encoded_path = os.path.join(base_path, path, "")
    return f"\nfsociety {encoded_path}# "


def run_tool(tool, selected_tool: str):
    if hasattr(tool, "install") and not tool.installed():
        tool.install()
    try:
        response = tool.run()
        if response and response > 0 and response != 256:
            console.error(f"{selected_tool} returned a non-zero exit code")
            if hasattr(tool, "install") and confirm("Do you want to reinstall?"):
                os.chdir(INSTALL_DIR)
                tool.uninstall()
                tool.install()
        console.success(f"{selected_tool} completed")
    except KeyboardInterrupt:
        return


def tools_cli(name, tools, links=True):
    table = Table(box=box.HEAVY_HEAD)
    table.add_column("Name", style="red", no_wrap=True)
    table.add_column("Description", style="magenta")
    if links:
        table.add_column("Link", no_wrap=True)

    tools_dict = {}
    for tool in tools:
        tools_dict[str(tool)] = tool
        args = [str(tool), tool.description]
        if links:
            text_link = Text(f"{tool.path}")
            text_link.stylize(Style(link=f"https://github.com/{tool.path}"))
            args.append(text_link)
        table.add_row(*args)

    console.print(table)
    console.command("back")
    set_readline(list(tools_dict.keys()) + BACK_COMMANDS)
    selected_tool = input(prompt(name.split(".")[-2])).strip()
    if selected_tool not in tools_dict:
        if selected_tool in BACK_COMMANDS:
            return
        if selected_tool == "exit":
            raise KeyboardInterrupt
        console.warn("Invalid Command")
        return tools_cli(name, tools, links)
    tool = tools_dict.get(selected_tool)
    return run_tool(tool, selected_tool)


def confirm(message="Do you want to?"):
    response = input(f"{message} (y/n): ").lower()
    if response:
        return response[0] == "y"
    return False
