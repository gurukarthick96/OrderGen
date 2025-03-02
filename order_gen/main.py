from fastapi import FastAPI

from order_gen.api import order_router, gen_router
from order_gen.db import ensure_indexes

app = FastAPI()
app.include_router(order_router)
app.include_router(gen_router)

ensure_indexes()


@app.get('/')
def root():
    return 'Hello World'
