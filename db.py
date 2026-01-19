import os

from dotenv import load_dotenv
from psycopg_pool import AsyncConnectionPool

_ = load_dotenv()

_pool: AsyncConnectionPool | None = None


def get_pool() -> AsyncConnectionPool:
    global _pool
    if _pool is None:
        _pool = AsyncConnectionPool(conninfo=os.environ["DATABASE_URL"], open=False)
    return _pool


async def close_pool():
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
