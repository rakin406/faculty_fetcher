import asyncio

from ..db import pool

SCHEMA_PATH = "migrations/001_init.sql"


async def migrate():
    try:
        with open(SCHEMA_PATH, "r") as file:
            content = file.read()

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


if __name__ == "__main__":
    asyncio.run(migrate())
