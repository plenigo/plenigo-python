import logging
import sys
from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5


logger = logging.getLogger("plenigo")


def log_message(log_level: LogLevel, message: str):
    if log_level == LogLevel.DEBUG:
        print(message, file=sys.stderr)
        logger.debug(message)
    elif log_level == LogLevel.INFO:
        logger.info(message)
    elif log_level == LogLevel.WARNING:
        logger.warning(message)
    elif log_level == LogLevel.ERROR:
        logger.error(message)
    elif log_level == LogLevel.FATAL:
        logger.fatal(message)
