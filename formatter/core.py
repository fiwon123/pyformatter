from formatter.registry import get_formatter
from formatter.utils import print_error, get_extension

def process_file(filepath: str, is_checking: bool = False, is_dry_run: bool = False, is_pretty: bool = False, in_place: bool = False):
    formatter_class = get_formatter(get_extension(filepath)[1:])

    if (formatter_class == None):
        print_error("Invalid input file.")

    formatter = formatter_class(filepath)

    if (is_checking):
        formatter.check()
    if (is_dry_run):
        formatter.dry_run()
    if (not is_checking and not is_dry_run):
        formatter.format(in_place)