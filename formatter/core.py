from formatter.utils import print_error, get_extension
from formatter import format_json, format_yaml

def process_file(filepath: str):
    extension = get_extension(filepath)     

    match (extension):
        case ".json":
            format_json(filepath)
        case ".yaml":
            format_yaml(filepath)
        case _:
            print_error("Invalid input file")
        