import uvicorn

from order_gen import app

host = '127.0.0.1'
port = 8000
environment = 'production'
# environment = 'development'

if __name__ == '__main__':

    is_production = environment == 'production'
    order_gen_app = app if is_production else 'order_gen:app'
    reload = not is_production

    try:
        print('starting app...')
        uvicorn.run(order_gen_app, host=host, port=port, reload=reload, workers=1)

    except Exception as e:
        print(f'caught error: {e}')

    finally:
        print('exiting app...')
