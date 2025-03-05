from order_gen.env import get_env

ENVIRONMENT = get_env('ENVIRONMENT')

SERVICE_NAME = get_env('SERVICE_NAME', 'OrderGen-App')
BASE_PATH = get_env('BASE_PATH', '/order-gen-app')

SERVER_HOST = get_env('SERVER_HOST')
SERVER_PORT = get_env('SERVER_PORT', required_type=int)
SERVER_RELOAD = get_env('SERVER_RELOAD', False, required_type=bool)
SERVER_MAX_WORKERS = get_env('SERVER_MAX_WORKERS', 1, required_type=int)

LOGGING_LEVEL = get_env('LOGGING_LEVEL', 'INFO')
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

DATABASE_URL = get_env('DATABASE_URL')
DATABASE_NAME = get_env('DATABASE_NAME')
ORDER_COLLECTION_NAME = get_env('ORDER_COLLECTION_NAME', 'AI_Order')

GEN_ORDERS_BATCH_SIZE = get_env('GEN_ORDERS_BATCH_SIZE', 1000, required_type=int)
EXECUTOR_MAX_WORKERS = get_env('EXECUTOR_MAX_WORKERS', 5, required_type=int)
