import logging
import sys

import coloredlogs

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger('OrderGen-App')

coloredlogs.install(logger=logger, fmt=LOG_FORMAT)
