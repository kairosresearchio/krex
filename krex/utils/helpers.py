from logging.handlers import TimedRotatingFileHandler
import os
import time
from datetime import datetime, timezone


def generate_timestamp(iso_format=False):
    if iso_format:
        return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    return int(time.time() * 10**3)


def config_logging(logging, logging_level, log_file: str = None):
    """Configures logging with UTC timestamp and optional daily rotating log files.

    Example log format:
        2025-03-07 19:42:04.849 UTC DEBUG my_logger: Log message

    Args:
        logging: Python logging module
        logging_level (int/str): Log level (e.g., 10 for DEBUG, 20 for INFO)
        log_file (str, optional): Base filename for logs (e.g., "my_log.log"). If provided, logs will rotate daily.
    """

    # Set UTC time format
    logging.Formatter.converter = time.gmtime

    # Define log format
    log_format = "%(asctime)s.%(msecs)03d UTC %(levelname)s %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Create log formatter
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # Configure logging to console
    logging.basicConfig(level=logging_level, format=log_format, datefmt=date_format)

    # If a log file is provided, enable daily log rotation
    if log_file:
        log_dir = os.path.dirname(log_file) or "."  # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Create a rotating file handler (daily rotation)
        file_handler = TimedRotatingFileHandler(
            filename=log_file,  # This will be the base filename
            when="midnight",  # Rotate at midnight
            interval=1,  # Rotate every 1 day
            backupCount=30,  # Keep the last 7 days of logs
            encoding="utf-8",  # Support Unicode logs
            utc=True,  # Use UTC for time-based rotation
        )

        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y-%m-%d"  # Filename suffix pattern
        logging.getLogger().addHandler(file_handler)
