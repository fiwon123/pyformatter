import os
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel

console = Console()

def error(msg: str):
    typer.echo(msg, err=True)
    raise typer.Exit(1)

def error_box(message: str):
    console.print(Panel(message, title="[red]Error[/red]", border_style="red"))

def get_extension(filepath: str):
    return os.path.splitext(filepath)[1]

def get_dir_path(filepath: str):
    return os.path.dirname(filepath)

def get_file_name(filepath: str):
    return os.path.splitext(os.path.basename(filepath))[0]

def create_dir(filepath: str):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def get_path(path: str):
    return Path(path)

def join_paths(base_path: str, sub_path: str):
    return os.path.join(base_path, sub_path)

def dir_path(filepath: str):
    if os.path.exists(filepath):
        return filepath
    else:
        error_box("Missing argument '[bold red]FILEPATH[/]'.")
        error(f"❌ File '{filepath}' not found.")