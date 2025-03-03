import random
from datetime import datetime, timedelta


def random_price(min_price: float, max_price: float) -> float:
    return round(random.uniform(min_price, max_price), 2)


def random_datetime(from_date: datetime, to_date: datetime) -> datetime:
    time_delta = to_date - from_date
    random_seconds = random.uniform(0, time_delta.total_seconds())
    return from_date + timedelta(seconds=random_seconds)
