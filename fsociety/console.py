from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

# Install Traceback
install()

# Console Setup
fsociety_theme = Theme(
    {
        "command": "black on white",
        "warning": "bold yellow",
    }
)
console = Console(theme=fsociety_theme)
