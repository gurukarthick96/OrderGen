from concurrent.futures import ThreadPoolExecutor

from order_gen import config

executor = ThreadPoolExecutor(max_workers=config.EXECUTOR_MAX_WORKERS)
