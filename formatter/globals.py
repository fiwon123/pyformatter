from formatter.formatter_logger import FormatterLogger

formatter_logger:FormatterLogger = None

def set_logger(logger):
    global formatter_logger
    formatter_logger = logger

def get_logger():
    return formatter_logger