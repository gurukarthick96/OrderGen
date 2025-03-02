import uuid
from datetime import datetime

from pydantic import BaseModel

from order_gen.db import OrderDomain


class Order(BaseModel):
    order_id: str
    total: float
    created_at: str

    def __init__(self, **kwargs):
        kwargs.setdefault('order_id', str(uuid.uuid4()))
        kwargs.setdefault('created_at', datetime.now().isoformat())
        super().__init__(**kwargs)

    def to_domain(self: 'Order') -> OrderDomain:
        return OrderDomain(order_id=self.order_id, total=self.total,
                           created_at=datetime.fromisoformat(self.created_at))

    @classmethod
    def from_domain(cls, order_domain: OrderDomain):
        return cls(order_id=order_domain.id, total=order_domain.total,
                   created_at=order_domain.created_at.isoformat())
