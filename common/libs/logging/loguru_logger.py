from loguru import logger
from .base_logger import BaseLogger

class LoguruLogger(BaseLogger):
    
    def debug(self, message: str):
        logger.debug(message)

    def info(self, message: str):
        logger.info(message)

    def warning(self, message: str):
        logger.warning(message)

    def error(self, message: str):
        logger.error(message)

    def critical(self, message: str):
        logger.critical(message)
