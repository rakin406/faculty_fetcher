import sys
from pathlib import Path
import asyncio

# Append the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from db import get_pool, close_pool

SCHEMA_PATH = "migrations/001_init.sql"


async def migrate():
    try:
        with open(SCHEMA_PATH, "r") as file:
            content = file.read()

        pool = get_pool()
        await pool.open()

        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(content)

        print("Migration completed")
    except FileNotFoundError:
        print(f"Error: The file '{SCHEMA_PATH}' was not found.")
        raise
    except Exception as e:
        print(f"Migration failed: {e}")
        raise
    finally:
        await close_pool()


if __name__ == "__main__":
    asyncio.run(migrate())
