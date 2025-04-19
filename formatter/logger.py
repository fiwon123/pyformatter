import datetime
import logging
from formatter.globals import log, configs

def save_log(msg: str):
    if log == None or configs["disable-log"]:
        return
    
    log.info(msg)


def get_logger():
    return log

def init_logger(disable_log: bool = False):
    from formatter.utils import get_path
    from formatter.globals import log

    if log != None:
        return log

    log = logging.getLogger("log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    
    log.setLevel(logging.INFO)

    if not disable_log:
        log_dir = get_path("logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%Hh%M")
        file_handler = logging.FileHandler(log_dir / f"formatter_{timestamp}.log")
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)