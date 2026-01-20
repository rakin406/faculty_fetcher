import os

from dotenv import load_dotenv
from psycopg_pool import ConnectionPool
from loguru import logger

_ = load_dotenv()

_pool: ConnectionPool | None = None


def get_pool() -> ConnectionPool:
    global _pool
    if _pool is None:
        logger.debug("Connecting to database")
        _pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"], open=False)
        logger.info("Connected to database")
    return _pool


def close_pool():
    global _pool
    if _pool is not None:
        logger.debug("Closing database connection")
        _pool.close()
        _pool = None
        logger.info("Database connection closed")
