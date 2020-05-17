MENU = """fsociety"""


def mainloop():
    print(MENU)
    input("Enter Command: ")


def cli():
    try:
        while True:
            mainloop()
    except KeyboardInterrupt:
        print("Exitting...")
        exit(0)


if __name__ == "__main__":
    cli()
