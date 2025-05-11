import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import text
from extract_char import extract_characters
from load.load_to_staging import load_to_staging
from db_utils import get_engine

def run_sql_script(path):
    engine = get_engine()
    with engine.begin() as conn:
        with open(path) as f:
            sql = f.read()
        # Split on semicolon to handle multiple statements
        for stmt in sql.split(";"):
            if stmt.strip():
                conn.execute(text(stmt))

def main():
    print("Creating tables if not exists...")
    run_sql_script("models/ddl_staging.sql")
    run_sql_script("models/ddl_dim.sql")

    print("Extracting characters...")
    extract_characters()

    print("Loading to staging...")
    load_to_staging("data/charlist.csv")

    print("Merging into dimension table...")
    run_sql_script("transform/merge_dim_character.sql")

    print("ETL pipeline complete.")

if __name__ == "__main__":
    main()