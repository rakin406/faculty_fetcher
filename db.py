import os

from dotenv import load_dotenv
from psycopg_pool import AsyncConnectionPool

_ = load_dotenv()

pool = AsyncConnectionPool(conninfo=os.environ["DATABASE_URL"], open=True)
