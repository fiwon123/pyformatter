import typer
from formatter.core import process_file

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the YAML or JSON file to format.")):
    process_file(filepath)