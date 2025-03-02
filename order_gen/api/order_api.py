from typing import List

from fastapi import HTTPException, APIRouter, Response

from order_gen import service as svc
from order_gen.api import Order
from order_gen.modules import logger

router = APIRouter(prefix='/orders', tags=['Orders'])


@router.post('', response_model=Order)
def create(order: Order) -> Order:
    if svc.get_order_by_id(order.order_id):
        logger.warning('create error :: Order ID already exists: %s', order.order_id)
        raise HTTPException(status_code=409, detail='Order ID already exists')
    return svc.create_order(order)


@router.get('', response_model=List[Order])
def get_all() -> list[Order]:
    return svc.get_orders()


@router.get('/{order_id}', response_model=Order)
def get_by_id(order_id: str) -> Order:
    if not (order := svc.get_order_by_id(order_id)):
        logger.warning('get_by_id error :: Order not found: %s', order_id)
        raise HTTPException(status_code=404, detail='Order not found')
    return order


@router.put('/{order_id}', response_model=Order)
def update(order_id: str, updated_order: Order) -> Order:
    if not svc.get_order_by_id(order_id):
        logger.warning('update error :: Order not found: %s', order_id)
        raise HTTPException(status_code=404, detail='Order not found')
    return svc.update_order(order_id, updated_order)


@router.delete('/{order_id}')
def delete(order_id: str) -> Response:
    if not svc.get_order_by_id(order_id):
        logger.warning('delete error :: Order not found: %s', order_id)
        raise HTTPException(status_code=404, detail='Order not found')
    svc.delete_order(order_id)
    return Response(status_code=204)
