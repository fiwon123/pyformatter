from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import get_formatter
from formatter.utils import print_error, get_extension, print_msg

def process_file(filepath: str, dir_output:str = None, is_checking: bool = False, is_dry_run: bool = False, is_pretty: bool = False, in_place: bool = False, file_type:str = None):
    
    print_msg("Verifying filepath...")
    if file_type != None:
        formatter_class = get_formatter(file_type)
        
        if formatter_class == None:
            print_error(f"Invalid parameter file_type: {file_type}")
    else:
        formatter_class = get_formatter(get_extension(filepath)[1:])
        
        if (formatter_class == None):
            print_error(f"Invalid input file: {filepath}")

    print_msg("Verification passed.")
    formatter:BaseFormatter = formatter_class(filepath)

    if (is_checking):
        formatter.check()
    if (is_dry_run):
        formatter.dry_run()
    if (not is_checking and not is_dry_run):
        formatter.format(dir_output, in_place)