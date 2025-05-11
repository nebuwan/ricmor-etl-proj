from .db_utils import get_engine
from sqlalchemy import text

def test_db():
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            for row in result:
                print("PostgreSQL version:", row[0])
        print("Connection successful!")
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    test_db()
