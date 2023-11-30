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

    def remove(self):
        logger.remove()

    def add(self, sink, *, level=None, format=None, filter=None, colorize=None, serialize=False, backtrace=False, diagnose=False, enqueue=False, catch=False, **kwargs):
        logger.add(sink, level=level, format=format, filter=filter, colorize=colorize, serialize=serialize, backtrace=backtrace, diagnose=diagnose, enqueue=enqueue, catch=catch, **kwargs)

    def patch(self, sink, *, level=None, format=None, filter=None, colorize=None, serialize=False, backtrace=False, diagnose=False, enqueue=False, catch=False, **kwargs):
        logger.patch(sink, level=level, format=format, filter=filter, colorize=colorize, serialize=serialize, backtrace=backtrace, diagnose=diagnose, enqueue=enqueue, catch=catch, **kwargs)

    def configure(self, *, handlers=None, levels=None, extra=None, patcher=None, activation=None, deactivate_existing_loggers=None, colorize=None, serialize=None, backtrace=None, diagnose=None, enqueue=None, exception=None, compression=None, rotation=None, retention=None, filter=None, format=None, level=None, sink=None,  catch=False, **kwargs):
        logger.configure(handlers=handlers, levels=levels, extra=extra, patcher=patcher, activation=activation, deactivate_existing_loggers=deactivate_existing_loggers, colorize=colorize, serialize=serialize, backtrace=backtrace, diagnose=diagnose, enqueue=enqueue, exception=exception, compression=compression, rotation=rotation, retention=retention, filter=filter, format=format, level=level, sink=sink,  catch=catch, **kwargs)
