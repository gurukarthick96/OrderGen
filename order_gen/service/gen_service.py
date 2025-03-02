import random
from datetime import datetime, timedelta

from order_gen.api import GenRequest
from order_gen.db import OrderDomain


def generate_orders(gen_request: GenRequest) -> None:
    for _ in range(gen_request.num_of_orders):
        order_domain = __generate_random_order(gen_request)
        order_domain.save()


def __generate_random_order(gen_request: GenRequest) -> OrderDomain:
    total = __random_price(gen_request.total_range[0], gen_request.total_range[1])
    created = __random_datetime(gen_request.created_range[0], gen_request.created_range[1])
    order_domain = OrderDomain(total=total, created_at=created)
    return order_domain


def __random_price(min_price: float, max_price: float) -> float:
    return round(random.uniform(min_price, max_price), 2)


def __random_datetime(from_date: datetime, to_date: datetime) -> datetime:
    time_delta = to_date - from_date
    random_seconds = random.uniform(0, time_delta.total_seconds())
    return from_date + timedelta(seconds=random_seconds)


def wipe_orders() -> None:
    OrderDomain.delete_all()
