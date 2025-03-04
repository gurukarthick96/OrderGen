import logging
import sys

import coloredlogs

from order_gen import config

logging.basicConfig(
    level=config.LOGGING_LEVEL,
    format=config.LOGGING_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(config.LOGGING_FILE)
    ]
)

logger = logging.getLogger(config.SERVICE_NAME)

coloredlogs.install(logger=logger, fmt=config.LOGGING_FORMAT)
