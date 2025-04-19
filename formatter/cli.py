import typer
from formatter.core import process_file
from formatter.formatter_logger import FormatterLogger
from formatter.globals import set_logger

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the file to format. (YAML, JSON, ...)"),
           disable_log: bool = typer.Option(False, "--disable-logs", help="Disable all logs while formatting the file."),
           check:bool = typer.Option(False, "--check", help="Check if current file is already formatted."),
           dry_run:bool = typer.Option(False, "--dry-run", help="Show a preview in the CLI without generate an output file."),
           in_place:bool = typer.Option(False, "--in-place", help="Overwrite the current file with the output."),
           file_type:str = typer.Option(None, "--type", "-t", help="Explicitly set file type in lowercase (example: 'json', 'yaml', ...)."),
           pretty: bool = typer.Option(False, "--pretty", help="CLI becomes more modern with colours, text boxes, previews becomes more readable and more.")):
       
       set_logger(FormatterLogger(disable_log, pretty))

       process_file(filepath, check, dry_run, pretty, in_place, file_type)