from order_gen.api import Order
from order_gen.db import OrderDomain


def create_order(order: Order) -> Order:
    order_domain = order.to_domain()
    order_domain.insert()

    return Order.from_domain(order_domain)


def get_orders() -> list[Order]:
    order_domains = OrderDomain.get_all()

    return [Order.from_domain(order_domain) for order_domain in order_domains]


def get_order_by_id(order_id: str) -> Order | None:
    order_domain = OrderDomain.get_by_id(order_id)

    return Order.from_domain(order_domain) if order_domain else None


def update_order(order_id: str, order: Order) -> Order:
    order_domain = OrderDomain.get_by_id(order_id)

    order_domain.total = order.total
    order_domain.update()

    return Order.from_domain(order_domain)


def delete_order(order_id: str) -> None:
    OrderDomain.delete(order_id)
