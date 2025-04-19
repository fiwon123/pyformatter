import typer
from formatter.core import process_file
from formatter.logger import init_logger
from formatter.utils import print_msg

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the YAML or JSON file to format."),
           disable_log: bool = typer.Option(False, "--disable-log", help="Disable all logs while formatting the file.")):
    init_logger(disable_log)
    process_file(filepath)