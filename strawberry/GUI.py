# GUI.py
# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
import platform
from dataclasses import dataclass
from shutil import get_terminal_size
from typing import Optional

# Rich UI
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align
from rich.markdown import Markdown
from rich.theme import Theme
from rich import box

# prompt_toolkit (input + completion opzionale)
try:
    from prompt_toolkit import prompt as pt_prompt
    from prompt_toolkit.completion import WordCompleter
    HAVE_PT = True
except Exception:
    HAVE_PT = False

# ----------------------------- Unicode/ASCII fallback -----------------------------
def _supports_unicode_stdout() -> bool:
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        "\u2500\u2588\u2022".encode(enc)
        return True
    except Exception:
        return False

UNICODE_OK = _supports_unicode_stdout()
BOX_STYLE = box.HEAVY if UNICODE_OK else box.ASCII
BULLET = "\u2022" if UNICODE_OK else "*"
DASH = "\u2014" if UNICODE_OK else "-"  # em dash -> hyphen se ASCII

# ----------------------------- Config Rich -----------------------------
theme = Theme(
    {
        "title": "bold magenta",
        "dim": "dim",
        "ok": "bold green",
        "warn": "bold yellow",
        "err": "bold red",
        "cmd": "bold cyan",
        "flag": "bold blue",
        "ver": "bold white",
    }
)
console = Console(theme=theme, soft_wrap=False)

# ----------------------------- Info App -----------------------------
@dataclass(frozen=True)
class infoStrawberry:  # compat
    version: str = "6.0.0"
    month_release: str = "December"
    year_release: str = "2022"

# ----------------------------- Back-compat ANSI (solo se servisse) -----------------------------
class textColors:  # mantenuto per retrocompatibilita'
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    SELECTED = "\033[7m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[93m"

# ----------------------------- Utils -----------------------------
def _clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def _app_header() -> Panel:
    title = "Jonio Strawberry File Administrator " + infoStrawberry.version
    subtitle = f"{infoStrawberry.month_release} {infoStrawberry.year_release}"
    sysline = (
        "Running on: "
        + sys.platform
        + " "
        + platform.system()
        + " "
        + platform.release()
        + " "
        + DASH
        + " Python "
        + platform.python_version()
    )
    body = Align.center(
        "[title]" + title + "[/title]\n[dim]" + subtitle + "[/dim]\n\n" + sysline,
        vertical="middle",
    )
    return Panel(body, border_style="magenta", box=BOX_STYLE)

def _section(title: str) -> Rule:
    return Rule(title, style="title")

def _cmd_table() -> Table:
    t = Table(box=BOX_STYLE, show_header=False, expand=False, padding=(0, 2))
    t.add_column(justify="left", style="flag", no_wrap=True)
    t.add_column(justify="left")
    t.add_row("-h, --help", "Mostra l'help ed esce")
    t.add_row("--version", "Stampa la versione")
    t.add_row("-eR [PATH]", "Reorder per estensione (elementary)")
    t.add_row("-aR PATH -e .EXT -d FOLDER", "Advanced Reorder (estensione e cartella di destinazione)")
    t.add_row("-kwR PATH -kw KEYWORD -d FOLDER", "Reorder per parola chiave")
    t.add_row("-bdR PATH -i YYYY-mm-dd -f YYYY-mm-dd -e .EXT", "Reorder per data (non Linux: birthtime; su Linux usare LbdR)")
    t.add_row("-fD PATH", "Ricerca file duplicati ricorsiva")
    return t

def _examples_md() -> Markdown:
    return Markdown(
        """\
**Esempi**
```bash
# Elementary reorder ricorsivo
strawberry -eR /path/dir

# Advanced reorder solo .pdf
strawberry -aR /path/dir -e .pdf -d PDF_ONLY

# Keyword reorder
strawberry -kwR /path/dir -kw bilancio -d CONTABILITA

# By date (non-Linux)
strawberry -bdR /path/dir -i 2023-01-01 -f 2023-12-31 -e .jpg

# Find duplicates
strawberry -fD /path/dir
```
""",
        code_theme="monokai",
    )

# ----------------------------- API schermo -----------------------------
def homeScreen() -> None:
    _clear()
    width = get_terminal_size((100, 30)).columns
    console.print(_app_header(), width=width)
    console.print(_section("Menu rapido"))
    items = [
        ("1", "Reorder per estensione"),
        ("2", "Advanced reorder"),
        ("3", "Reorder per keyword"),
        ("4", "Reorder per data"),
        ("5", "Cerca duplicati"),
        ("h", "Help"),
        ("q", "Esci"),
    ]
    tbl = Table(box=BOX_STYLE, show_header=False, expand=False)
    tbl.add_column("Key", justify="center", style="cmd", no_wrap=True)
    tbl.add_column("Azione", style="ver")
    for k, label in items:
        tbl.add_row(k, label)
    console.print(tbl)

def helpPage() -> None:
    _clear()
    console.print(_app_header())
    console.print(_section("Comandi"))
    console.print(_cmd_table())
    console.print(_section("Esempi"))
    console.print(_examples_md())

# ----------------------------- Prompt interattivo -----------------------------
def prompt_choice(prompt_text: str = "Seleziona un'opzione") -> str:
    choices = ["1", "2", "3", "4", "5", "h", "q"]
    if HAVE_PT:
        from prompt_toolkit.completion import WordCompleter
        completer = WordCompleter(choices, ignore_case=True, sentence=True)
        try:
            ans = pt_prompt(f"{prompt_text} [{'/'.join(choices)}]: ", completer=completer).strip()
        except Exception:
            ans = input(f"{prompt_text} [{'/'.join(choices)}]: ").strip()
    else:
        ans = input(f"{prompt_text} [{'/'.join(choices)}]: ").strip()
    return ans or "q"

# ----------------------------- Version helper -----------------------------
def print_version() -> None:
    console.print(
        "Jonio Strawberry File Administrator "
        "[ver]" + infoStrawberry.version + "[/ver] "
        "(" + infoStrawberry.month_release + " " + infoStrawberry.year_release + ")"
    )

# ----------------------------- Demo run (facoltativo) -----------------------------
if __name__ == "__main__":
    homeScreen()
    c = prompt_choice()
    if c.lower() in {"h", "help", "--help", "-h"}:
        helpPage()
    elif c.lower() in {"q", "quit", "exit"}:
        pass
    else:
        console.print("Hai scelto: [cmd]" + c + "[/cmd]")