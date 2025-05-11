from extract_char import extract_characters
from load.load_to_staging import load_to_staging
from db_utils import get_engine

def run_sql_script(path):
    engine = get_engine()
    with engine.begin() as conn:
        with open(path) as f:
            sql = f.read()
        conn.execute(sql)

def main():
    print("Starting ETL pipeline...")
    extract_characters()
    load_to_staging("data/charlist.csv")
    run_sql_script("transform/merge_dim_character.sql")
    print("ETL pipeline complete.")

if __name__ == "__main__":
    main()