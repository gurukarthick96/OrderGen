bind = '0.0.0.0:8000'

workers = 2

worker_class = 'uvicorn.workers.UvicornWorker'

timeout = 120
graceful_timeout = 90
keepalive = 5

proc_name = 'OrderGen-App'

preload_app = False

backlog = 1024
