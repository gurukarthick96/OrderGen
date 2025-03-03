import asyncio

import order_gen.config as config
from order_gen.api import GenRequest
from order_gen.db import OrderDomain
from order_gen.modules import executor, random_price, random_datetime

batch_size = config.GEN_ORDERS_BATCH_SIZE


def generate_orders(gen_request: GenRequest) -> None:
    asyncio.run(_generate_orders_async(gen_request))


def _generate_orders_single_batch(gen_request: GenRequest) -> None:
    __generate_orders_batch(gen_request, gen_request.num_of_orders)


def _generate_orders_sync(gen_request: GenRequest) -> None:
    count = gen_request.num_of_orders

    while count > 0:
        mod = min(batch_size, count)
        count -= mod

        __generate_orders_batch(gen_request, mod)


async def _generate_orders_async(gen_request: GenRequest) -> None:
    count = gen_request.num_of_orders

    tasks = []

    while count > 0:
        mod = min(batch_size, count)
        count -= mod

        task = asyncio.create_task(__generate_orders_async_task(gen_request, mod))
        tasks.append(task)

    await asyncio.gather(*tasks)


async def __generate_orders_async_task(gen_request: GenRequest, mod: int) -> None:
    loop = asyncio.get_running_loop()

    await loop.run_in_executor(executor, __generate_orders_batch, gen_request, mod)


def __generate_orders_batch(gen_request: GenRequest, mod: int) -> None:
    order_domains = [__generate_random_order(gen_request) for _ in range(mod)]

    OrderDomain.insert_many(order_domains)


def __generate_random_order(gen_request: GenRequest) -> OrderDomain:
    return OrderDomain(
        total=random_price(*gen_request.total_range),
        created_at=random_datetime(*gen_request.created_range)
    )


def wipe_orders() -> None:
    OrderDomain.delete_all()
