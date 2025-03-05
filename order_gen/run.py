import uvicorn

import order_gen.config as config
from order_gen.modules import logger


def run_locally():
    try:
        logger.info('starting app locally...')
        uvicorn.run(
            app='order_gen:app',
            host=config.SERVER_HOST,
            port=config.SERVER_PORT,
            reload=config.SERVER_RELOAD,
            workers=config.SERVER_MAX_WORKERS,
            log_config=None
        )

    except:
        logger.error('caught unexpected error while running app', exc_info=True)

    finally:
        logger.info('exiting app...')


if __name__ == '__main__':
    if config.ENVIRONMENT == 'local':
        run_locally()
    else:
        logger.warning('environment has to be local to start the app')
