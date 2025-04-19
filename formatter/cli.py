from formatter import yaml_formatter, json_formatter
import typer
from formatter.core import process_file
from formatter.logger import init_logger
from formatter.globals import configs

app = typer.Typer()

@app.command()
def format(filepath: str = typer.Argument(..., help="Path to the YAML or JSON file to format."),
           disable_log: bool = typer.Option(False, "--disable-logs", help="Disable all logs while formatting the file."),
           check:bool = typer.Option(False, "--check", help="Check if current file is already formatted."),
           dry_run:bool = typer.Option(False, "--dry-run", help="Show a preview in the CLI without generate an output file."),
           pretty: bool = typer.Option(False, "--pretty", help="CLI becomes more modern with colours, text boxes, previews becomes more readable and more.")):
    configs["disable-logs"] = disable_log
    configs["dry-run"] = dry_run
    configs["check"] = check
    configs["pretty"] = pretty

    init_logger(disable_log, pretty)
    process_file(filepath, check, dry_run, pretty)