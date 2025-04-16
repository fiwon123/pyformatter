import typer
from formatter.core import process_file
from formatter.logger import get_logger

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the YAML or JSON file to format.")):
    log = get_logger("Test", True)
    log.info("Formatting started")

    process_file(filepath)