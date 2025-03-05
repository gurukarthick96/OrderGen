import socket

from fastapi import APIRouter, Depends

from order_gen.db.database import order_db

router = APIRouter(prefix='/internal')


@router.get('/ping')
def ping():
    return {
        'healthy': True,
        'hostname': socket.gethostname()
    }


async def check_database():
    try:
        order_db.command('ping')
        return True
    except:
        return False


@router.get('/health')
async def health_check(db: bool = Depends(check_database)):
    return {
        'healthy': True if db else False,
        'database': db,
        'hostname': socket.gethostname(),
    }
