
import logging
from datetime import datetime
from pathlib import Path

from rich.logging import RichHandler

class Logger:
    """Application logger configurator"""

    @staticmethod
    def setup() -> None:
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d")
        log_file = log_dir / f"log_{timestamp}.log"
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        dateformat = "%Y-%m-%d %H:%M:%S"
        format = "%(asctime)s %(levelname)s %(name)s: %(message)s"
        file_handler.setFormatter(logging.Formatter(format,datefmt=dateformat))
        
        console_handler = RichHandler(rich_tracebacks=True)
        console_handler.setLevel(logging.CRITICAL) 
        console_handler.setFormatter(logging.Formatter('%(message)s'))
        
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)