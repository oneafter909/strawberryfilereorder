from importlib.metadata import version
import os
import sys
from os import listdir
from os.path import isfile, join
import shutil

# --- Rich for nicer console output --- #
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

# --- App imports --- #
from GUI import textColors
from reorderutility import eR, aR, kwR, bdR, LbdR
from identifier import SearchDuplicate
from GUI import homeScreen, helpPage, infoStrawberry

# --- Setup --- #
console = Console()
version = infoStrawberry.version


def banner():
    console.print(
        Panel.fit(
            "[bold magenta]🍓 Strawberry Utility[/bold magenta]\n"
            f"[cyan]Version:[/cyan] [bold]{version}[/bold]\n",
            border_style="magenta",
        )
    )


def switchApp(i):
    if i == 1:
        eR("", False)
    elif i == 2:
        aR("", "", "")
    elif i == 3:
        kwR("", "", "")
    elif i == 4:
        if sys.platform != "linux":
            bdR("", "", "", "")
        else:
            LbdR("", "", "", "")
    elif i == 5:
        SearchDuplicate("")
    else:
        console.print("[bold red]⚠️  Command not recognized[/bold red]")


def begin():
    os.system("clear" if sys.platform != "win32" else "cls")
    banner()
    homeScreen()

    # Argument handling
    if sys.argv[1:]:
        try:
            if sys.argv[1] in ("--help", "-h"):
                helpPage()
                sys.exit()
            if sys.argv[1] == "--version":
                console.print(f"[green]{version}[/green]")
                sys.exit()
        except Exception:
            console.print("[bold red]❌ An error occurred parsing arguments.[/bold red]")
            if sys.argv[1] == "-help":
                console.print("[yellow]Tip:[/yellow] Use '--help' to view usage.")
                sys.exit()

    if sys.argv[8:]:
        if sys.argv[1] in ("-bdR", "--bydateReorder"):
            if sys.platform == "linux":
                LbdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])
            else:
                bdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])

    if sys.argv[6:]:
        if sys.argv[1] in ("-kwR", "--keywordReorder"):
            kwR(sys.argv[2], sys.argv[4].replace("_", " "), sys.argv[6].replace("_", " "))
        if sys.argv[1] in ("-aR", "--advancedReorder"):
            aR(sys.argv[2], sys.argv[4], sys.argv[6].replace("_", " "))

    if sys.argv[3:]:
        if sys.argv[1] in ("-eR", "--elementaryReorder") and sys.argv[3] == "-R":
            eR(sys.argv[2], True)

    if sys.argv[2:]:
        if sys.argv[1] in ("-eR", "--elementaryReorder"):
            eR(sys.argv[2], False)
        elif sys.argv[1] in ("-fD", "--findDuplicated"):
            SearchDuplicate(sys.argv[2])

    # No args given: interactive mode
    console.print(
        Panel.fit("[bold cyan]Select a reordering mode:[/bold cyan]", border_style="cyan")
    )

    table = Table(title="Available Modes", box=box.SIMPLE_HEAVY)
    table.add_column("Option", justify="center", style="bold yellow")
    table.add_column("Description", style="white")

    table.add_row("1", "Reorder by extension")
    table.add_row("2", "Advanced reorder")
    table.add_row("3", "Reorder by keyword")
    table.add_row("4", "Reorder by date")
    table.add_row("5", "Search duplicate files")

    console.print(table)

    try:
        iP = Prompt.ask("[bold green]Enter a mode[/bold green]", default="1")
        switchApp(int(iP))
    except KeyboardInterrupt:
        console.clear()
        sys.exit()
    except ValueError:
        console.print("[bold red]Invalid input. Please enter a number between 1–5.[/bold red]")
        sys.exit()


if __name__ == "__main__":
    begin()
