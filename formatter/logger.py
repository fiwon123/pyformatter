import datetime
import logging

log:logging.Logger = None
disable = False

def save_log(msg: str):
    global log
    global disable

    if log == None or disable:
        return
    
    log.info(msg)


def get_logger():
    global log
    return log

def init_logger(disable_log: bool = False):
    from formatter.utils import get_path
    global log
    global disable

    disable = disable_log

    if log != None:
        return log

    log = logging.getLogger("log")

    # handler = logging.StreamHandler()
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