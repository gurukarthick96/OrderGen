from fastapi import APIRouter, Response

from order_gen import service as svc
from order_gen.api import GenRequest
from order_gen.modules import logger

router = APIRouter(prefix='/gen', tags=['Generative'])


@router.post('/orders')
def generate_order(gen_request: GenRequest) -> Response:
    logger.info('generating orders with: %s', gen_request)
    svc.generate_orders(gen_request)
    return Response(status_code=200)


@router.delete('/orders/wipe')
def wipe_orders() -> Response:
    logger.info('wiping out all orders')
    svc.wipe_orders()
    return Response(status_code=204)
