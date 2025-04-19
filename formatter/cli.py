import typer
from formatter.core import process_file
from formatter.logger import get_logger

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the YAML or JSON file to format."),
           save_log: bool = typer.Argument(False, help="Save all logs while formatting the file.")):
    log = get_logger("logger", save_log)
    log.info("Formatting started")

    process_file(filepath)