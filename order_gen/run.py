import uvicorn

from order_gen import app
from order_gen.modules import logger

host = '127.0.0.1'
port = 8000
environment = 'production'
# environment = 'development'

if __name__ == '__main__':

    is_production = environment == 'production'
    order_gen_app = app if is_production else 'order_gen:app'
    reload = not is_production

    try:
        logger.info('starting app...')
        uvicorn.run(order_gen_app, host=host, port=port, reload=reload, workers=1)

    except Exception as e:
        logger.error('caught error', e)

    finally:
        logger.info('exiting app...')
