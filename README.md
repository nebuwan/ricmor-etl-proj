# 🧬 Rick and Morty ETL Project

This project extracts character data from the [Rick and Morty API](https://rickandmortyapi.com/), loads it into a **PostgreSQL staging table**, and applies **Slowly Changing Dimension (SCD) Type 2** logic to maintain historical records in a dimension table.

It is designed using modular Python scripts for easy maintenance and scalability.

---

## 📁 Project Structure

```
rick_etl_project/
├── .env                         # Environment variables for PostgreSQL
├── extract_char.py              # Extract: Fetches character data from API
├── db_utils.py                  # Utility: Connects to PostgreSQL via SQLAlchemy
├── load/
│   └── load_to_staging.py       # Load: Pushes CSV to staging table
├── transform/
│   └── merge_dim_character.sql  # Transform: SQL logic for SCD Type 2 merge
├── models/
│   ├── ddl_staging.sql          # SQL: Create staging table
│   └── ddl_dim.sql              # SQL: Create dimension table
├── etl/
│   └── run_pipeline.py          # Orchestration script for the ETL process
└── data/
    └── charlist.csv             # Extracted character data as CSV
```

---

## ⚙️ Setup Instructions (macOS)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rick-etl-project.git
cd rick-etl-project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file at the project root:

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sandbox
```

### 5. Create PostgreSQL tables

Run these in your database:

```sql
-- Create staging and dimension schemas/tables
\i models/ddl_staging.sql
\i models/ddl_dim.sql
```

### 6. Run the pipeline

```bash
python etl/run_pipeline.py
```

---

## 💡 What the Pipeline Does

1. **Extract**: API → CSV (`data/charlist.csv`)
2. **Load**: CSV → `staging.rick_and_morty_characters`
3. **Transform**: Applies SCD2 logic → `dim.dim_character`

---

## 🛠 Technologies Used

- Python (pandas, requests, SQLAlchemy)
- PostgreSQL 15+
- SQL DDL and DML (with `MERGE`)
- `.env` configuration via `python-dotenv`

---

## 📊 Sample Output (dim.dim_character)

| character_key | character_name  | episode_count | is_current | effective_date | end_date  |
|---------------|------------------|---------------|------------|----------------|-----------|
| 1             | Rick Sanchez     | 51            | true       | 2025-05-10     | NULL      |
| 2             | Morty Smith      | 50            | false      | 2024-12-01     | 2025-05-01 |

---

## 🔒 Notes

- Requires PostgreSQL version 15 or higher for native `MERGE` support.
- `MERGE` script handles SCD2 logic with `is_current`, `end_date`, and `effective_date`.

---

## ✅ Future Enhancements

- Airflow integration for scheduling
- Logging and monitoring
- API schema validation
- Unit tests and coverage reports

---

## 🙌 Acknowledgements

- [Rick and Morty API](https://rickandmortyapi.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)