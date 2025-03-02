from pymongo import MongoClient, ASCENDING

from order_gen import config

print('connecting to database...')
client = MongoClient(config.DATABASE_URL)

order_db = client[config.DATABASE_NAME]

order_collection = order_db[config.ORDER_COLLECTION_NAME]


def ensure_indexes():
    print('ensuring indexes...')
    order_collection.create_index([('created_at', ASCENDING)])


if __name__ == '__main__':
    ensure_indexes()
