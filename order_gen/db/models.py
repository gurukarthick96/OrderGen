import uuid
from datetime import datetime

from pymongo import ASCENDING

from order_gen.db.database import order_collection
from order_gen.modules import logger


class OrderDomain:
    id: str
    total: float
    created_at: datetime

    def __init__(self, order_id: str = None, total: float = 0.0, created_at: datetime = None):
        self.id = order_id or str(uuid.uuid4())
        self.total = round(total, 2)
        self.created_at = created_at or datetime.now()

    def insert(self) -> str:
        order_doc = self.to_dict()
        order_collection.insert_one(order_doc)
        logger.info('Order inserted: %s', order_doc)
        return self.id

    def update(self) -> str:
        order_doc = self.to_dict()
        order_collection.update_one({'_id': self.id}, {'$set': order_doc})
        logger.info('Order updated: %s', order_doc)
        return self.id

    @staticmethod
    def insert_many(order_domains: list['OrderDomain']) -> None:
        order_docs = [order_domain.to_dict() for order_domain in order_domains]
        order_collection.insert_many(order_docs)
        logger.info('%s Order(s) inserted', len(order_domains))

    @staticmethod
    def get_by_id(order_id) -> 'OrderDomain | None':
        order_doc = order_collection.find_one({'_id': order_id})
        return OrderDomain.from_dict(order_doc) if order_doc else None

    @staticmethod
    def get_all() -> list['OrderDomain']:
        order_docs = order_collection.find({}).sort('created_at', ASCENDING)
        return [OrderDomain.from_dict(order_doc) for order_doc in order_docs]

    @staticmethod
    def delete(order_id) -> None:
        order_collection.delete_one({'_id': order_id})
        logger.info('Order deleted: %s', order_id)

    @staticmethod
    def delete_all() -> None:
        order_collection.delete_many({})
        logger.info('All Orders deleted')

    @classmethod
    def from_dict(cls, order_doc: dict) -> 'OrderDomain':
        return cls(order_id=order_doc['_id'], total=order_doc['total'], created_at=order_doc['created_at'])

    def to_dict(self) -> dict:
        return {
            '_id': self.id,
            'total': self.total,
            'created_at': self.created_at
        }
