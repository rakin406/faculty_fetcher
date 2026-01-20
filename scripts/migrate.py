import sys
from pathlib import Path

# Append the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from db import get_pool, close_pool

SCHEMA_PATH = "migrations/001_init.sql"


def migrate():
    try:
        with open(SCHEMA_PATH, "r") as file:
            content = file.read()

        pool = get_pool()
        pool.open()

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(content)

        print("Migration completed")
    except FileNotFoundError:
        print(f"Error: The file '{SCHEMA_PATH}' was not found.")
        raise
    except Exception as e:
        print(f"Migration failed: {e}")
        raise
    finally:
        close_pool()


if __name__ == "__main__":
    migrate()
