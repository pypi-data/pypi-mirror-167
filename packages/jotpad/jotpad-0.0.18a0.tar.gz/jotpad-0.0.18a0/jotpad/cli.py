import os
import sys

import fileinput
import functools
from pathlib import Path
from typing import Optional
import time

import typer
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

from .config import Config


app = typer.Typer()
APP_NAME = "jotpad"
APP_AUTHOR = "jotpad"


def get_paths(config):
    return sorted(Path(config.home).iterdir(), key=os.path.getmtime, reverse=True)


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    n: int = typer.Option(1, "--note-index", "-n"),
    dump: bool = typer.Option(False, "--dump", "-d"),
):  
    if not ctx.invoked_subcommand:
        config = Config()
        console = Console()
        paths = get_paths(config)

        if not len(paths):
            name = f"note-{len(paths) + 1}.{config.default_extension}"
            note_path = os.path.join(f"{config.home}", name)

            with open(note_path, "w") as f:
                f.write("")
        
        else:
            note_path = paths[n - 1]

        if not os.isatty(0):
            content = functools.reduce(lambda a, b: a + b, fileinput.input(files=()))

            with open(note_path, "a") as f:
                f.write(f"\n{content}")

        if dump:
            with open(note_path, "r") as f:
                note = f.read()
            console.print(note)
        else:
            os.system(f"{config.editor} {note_path}")


@app.command()
def new(
    dump: bool = typer.Option(False, "--dump", "-d"),
):
    console = Console()
    config = Config()
    name = f"note-{len(get_paths(config)) + 1}.{config.default_extension}"
    note_path = os.path.join(f"{config.home}", name)

    if not os.isatty(0):
        content = functools.reduce(lambda a, b: a + b, fileinput.input(files=()))
    else:
        content = ""
    
    with open(note_path, "w") as f:
        f.write(content)

    if dump:
        console.print(content)
    else:
        os.system(f"{config.editor} {note_path}")


@app.command()
def rm(
    ctx: typer.Context,
    n: int,
):  
    if not ctx.invoked_subcommand:
        config = Config()
        console = Console()
        paths = get_paths(config)
        note_path = paths[n - 1]
        os.remove(note_path)


@app.command()
def ls():
    console = Console()
    config = Config()
    paths = get_paths(config)

    table = Table(title="Notes")
    table.add_column("index", justify="right")
    table.add_column("modified")
    table.add_column("content")

    with console.pager():
        for i, p in enumerate(paths):
            modified = time.ctime(os.path.getmtime(p))

            with open(p, "r") as f:
                note = f.read()
                first = note.split("\n")[0]
                first = first if len(first) < 90 else f"{first[:87]}..."
            table.add_row(f"{i + 1}", modified,  f"{first}")
        console.print(table)


@app.command()
def config(
    editor: Optional[str] = typer.Option(None, "--editor", "-e"),
    home: Optional[str] = typer.Option(None, "--home", "-h"),
    init: Optional[bool] = typer.Option(False, "--init", "-i"),
    default_extension: Optional[str] = typer.Option(None, "--ext", "-x"),
):
    config = Config()
    console = Console()

    if init:
        config.init()
    if editor:
        config.editor = editor
    if home:
        config.home = home
    if default_extension:
        config.default_extension = default_extension

    table = Table(title="Config")
    table.add_column("key", justify="right")
    table.add_column("value")
    table.add_row("home", config.home)
    table.add_row("editor", config.editor)
    table.add_row("default_extension", config.default_extension)
    console.print(table)


if __name__ == "__main__":
    app()
