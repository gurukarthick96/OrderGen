from fastapi import FastAPI

from order_gen import config
from order_gen.api import internal_router, order_router, gen_router
from order_gen.db import ensure_indexes

app = FastAPI(root_path=config.BASE_PATH)
app.include_router(internal_router)
app.include_router(order_router)
app.include_router(gen_router)

ensure_indexes()


@app.get('/')
def root():
    return 'Hello World'
