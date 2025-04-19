from rich.logging import RichHandler
import datetime
import logging

class FormatterLogger:
    def __init__(self, disable_log: bool = False, pretty: bool = False):
        from formatter.utils import get_path

        self.disable_log = disable_log

        if pretty:
            logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
            self.logger = logging.getLogger("rich")
        else:
            self.logger = logging.getLogger("log")
        
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        self.logger.setLevel(logging.INFO)

        if not disable_log:
            log_dir = get_path("logs")
            log_dir.mkdir(exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%Hh%M")
            file_handler = logging.FileHandler(log_dir / f"formatter_{timestamp}.log")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            

    def save_log(self, msg: str):
        if self.logger == None or self.disable_log:
            return
        
        self.logger.info(msg)


    def get_logger(self):
        return self.logger
