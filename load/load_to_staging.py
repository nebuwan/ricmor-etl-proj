import pandas as pd
from db_utils import get_engine

def load_to_staging(csv_path):
    df = pd.read_csv(csv_path)
    engine = get_engine()
    with engine.begin() as conn:
