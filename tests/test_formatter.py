from formatter.logger import get_logger
from formatter.main import process_file

log = get_logger("Test", True)

def test_case():
    input_json = ".\\tests\\test.json"
    input_yaml = ".\\tests\\test.yaml"

    log.info("Formatting started")

    process_file(input_json)
    process_file(input_yaml)