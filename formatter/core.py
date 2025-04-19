from formatter.utils import print_error, get_extension
from formatter import format_json, check_json, format_yaml, check_yaml, dry_run_json, dry_run_yaml

def process_file(filepath: str, is_checking: bool = False, is_dry_run: bool = False, is_pretty: bool = False):
    extension = get_extension(filepath)     

    match (extension):
        case ".json":
            if (is_checking):
                check_json(filepath)
            if (is_dry_run):
                dry_run_json(filepath)
            if (not is_checking and not is_dry_run):
                format_json(filepath)
        case ".yaml":
            if (is_checking):
                check_yaml(filepath)
            if (is_dry_run):
                dry_run_yaml(filepath)
            if (not is_checking and not is_dry_run):
                format_yaml(filepath)
        case _:
            print_error("Invalid input file")
        