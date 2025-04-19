import os
from formatter.core import process_file
from formatter.formatter_logger import FormatterLogger
from formatter.globals import set_logger
from formatter.utils import print_msg

def test_case():
    folder_path = ".\\tests\\tests_toml"

    set_logger(FormatterLogger())

    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    print_msg(files)

    for f in files:
        process_file(f)