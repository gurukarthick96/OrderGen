import logging
import logging.handlers
import os

import coloredlogs

from order_gen import config

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

os.makedirs(LOG_DIR, exist_ok=True)


def get_global_logger():
    app_logger = logging.getLogger(config.SERVICE_NAME)

    loggers = [app_logger, *get_additional_loggers()]

    configure_loggers(loggers)

    return app_logger


def get_additional_loggers() -> list[logging.Logger]:
    return [
        get_customized_logger('uvicorn.access', 'Uvicorn-Api'),
        get_customized_logger('uvicorn.error', 'Uvicorn-Server'),
        get_customized_logger('gunicorn.access', 'Gunicorn-Api'),
        get_customized_logger('gunicorn.error', 'Gunicorn-Server')
    ]


def get_customized_logger(original_name, custom_name) -> logging.Logger:
    custom_logger = logging.getLogger(original_name)
    custom_logger.name = custom_name
    return custom_logger


def configure_loggers(loggers: list[logging.Logger]) -> None:
    if loggers[0].hasHandlers():
        return

    formatter = logging.Formatter(config.LOGGING_FORMAT)

    file_handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)

    for _logger in loggers:
        _logger.setLevel(config.LOGGING_LEVEL)
        _logger.addHandler(file_handler)
        coloredlogs.install(level=config.LOGGING_LEVEL, logger=_logger, fmt=config.LOGGING_FORMAT)


logger = get_global_logger()

logger.info('logger initialized successfully...')
