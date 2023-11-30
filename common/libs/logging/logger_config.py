import sys
from .loguru_logger import LoguruLogger

def setup_logger(log_level="INFO", log_to_file=False, file_path="app.log", rotation="1 week", format_string=None, external_config=None):
    """
    Configures the logging system.
    
    :param log_level: Log level (e.g., "INFO", "DEBUG", "ERROR").
    :param log_to_file: Boolean to enable logging to a file.
    :param file_path: Path to the log file (used if log_to_file is True).
    :param rotation: Log file rotation policy.
    :param format_string: Custom format string for log messages.
    :param external_config: Additional configurations for external logging systems.
    """
    logger = LoguruLogger()

    # Define default format if not provided
    if not format_string:
        format_string = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"

    # Remove default logger and add stdout with specified level and format
    logger.remove()
    logger.add(sys.stdout, level=log_level, format=format_string)

    # File logging
    if log_to_file:
        logger.add(file_path, rotation=rotation, level=log_level, format=format_string)

    # External logging systems (e.g., Sentry, Logstash)
    if external_config:
        setup_external_logging(logger, external_config)

    return logger

def setup_external_logging(logger, config):
    """
    Sets up external logging systems based on provided configuration.

    :param logger: The logger instance.
    :param config: Configuration dictionary for external logging systems.
    """
    # Example: Integrating with Sentry
    if "sentry_dsn" in config:
        import sentry_sdk
        from sentry_sdk.integrations.logging import LoggingIntegration
        sentry_logging = LoggingIntegration(level=config.get("sentry_level", "ERROR"), event_level=config.get("sentry_event_level", "ERROR"))
        sentry_sdk.init(dsn=config["sentry_dsn"], integrations=[sentry_logging])
    
    # Add more external logging systems here based on the config
