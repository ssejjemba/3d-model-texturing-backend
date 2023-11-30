from .loguru_logger import LoguruLogger
import sys

def setup_logger(log_level="INFO", output="console", file_path="app.log", rotation="1 week", format="{time} {level} {message}"):
    """
    Configures the logging system.
    
    :param log_level: Log level (e.g., "INFO", "DEBUG", "ERROR").
    :param output: Output destination ("console" or "file").
    :param file_path: Path to the log file (used if output is "file").
    :param rotation: Rotation policy for file logging.
    :param format: Log message format.
    """
    logger = LoguruLogger()
    logger.remove()  # Remove default logger

    # Console logging
    if output == "console":
        logger.add(sys.stdout, level=log_level, format=format)

    # File logging
    elif output == "file":
        logger.add(file_path, rotation=rotation, level=log_level, format=format)

    # Additional configuration can be added here for other outputs if needed

    return logger
