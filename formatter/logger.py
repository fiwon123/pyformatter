from rich.logging import RichHandler
import datetime
import logging
from formatter.globals import log, configs

def save_log(msg: str):
    if log == None or configs["disable-log"]:
        return
    
    log.info(msg)


def get_logger():
    return log

def init_logger(disable_log: bool = False, pretty: bool = False):
    from formatter.utils import get_path
    global log

    if log != None:
        return log

    if pretty:
        logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
        log = logging.getLogger("rich")
    else:
        log = logging.getLogger("log")

    print(log)
    
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