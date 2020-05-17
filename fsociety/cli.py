#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Core
from fsociety.menu import set_readline

# Modules
import fsociety.information_gathering
import fsociety.passwords

# Menu
MENU_TITLE = """
888888 .dP"Y8  dP"Yb   dP""b8 88 888888 888888 Yb  dP 
88__   `Ybo." dP   Yb dP   `" 88 88__     88    YbdP  
88""   o.`Y8b Yb   dP Yb      88 88""     88     8P   
88     8bodP'  YbodP   YboodP 88 888888   88    dP    

"""
MENU_ITEMS = [fsociety.information_gathering, fsociety.passwords]
items = dict()

# Menu


def command_name(module):
    return module.__name__.split(".")[-1]


def menutools(module):
    return "\n".join(["\t" + tool for tool in module.__tools__])


def menuitems():
    items_str = str()
    for value in MENU_ITEMS:
        name = command_name(value)
        tools = menutools(value)
        items_str += f"{name}: \n{tools}\n\n"
    return items_str


for item in MENU_ITEMS:
    items[command_name(item)] = item


def mainloop():
    print(MENU_TITLE)
    print(menuitems())
    selected_command = input("Enter Command: ").strip()
    if not selected_command:
        return
    print()
    try:
        func = items[selected_command].cli
        func()
    except Exception as e:
        print(str(e))


# CLI
def cli():
    try:
        while True:
            set_readline(items.keys())
            mainloop()
    except KeyboardInterrupt:
        print("\nExitting...")
        exit(0)


if __name__ == "__main__":
    cli()
