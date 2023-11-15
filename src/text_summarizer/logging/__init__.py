import os
import sys
import logging

LOGGER_NAME = "text_summarizer"
log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= log_format,
    handlers=[
        logging.FileHandler(log_filepath), # log to file
        logging.StreamHandler(sys.stdout) # log to terminal
    ]
)

logger = logging.getLogger(LOGGER_NAME)