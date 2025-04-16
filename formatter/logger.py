import datetime
import logging
from formatter.utils import get_path

def get_logger(name: str, log_to_file: bool = False) -> logging.Logger:
    logger = logging.getLogger(name)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Optional: file log
    if log_to_file:
        log_dir = get_path("logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%Hh%M")
        file_handler = logging.FileHandler(log_dir / f"formatter_{timestamp}.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger