# Rick and Morty ETL Project

This project extracts character data from the [Rick and Morty API](https://rickandmortyapi.com/), loads it into a PostgreSQL staging table, and applies Slowly Changing Dimension (SCD) Type 2 logic to maintain historical records in a dimension table.

## Project Structure

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

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rick-etl-project.git
cd rick-etl-project
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file at the project root:

```env
DB_USER=admin
DB_PASSWORD=admin123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sandbox
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=sandbox
POSTGRES_DATA=/your/local/path/postgres/data
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin123
PGADMIN_DATA=/your/local/path/pgadmin/data
```

Update paths for `POSTGRES_DATA` and `PGADMIN_DATA` as needed.

### 5. Start PostgreSQL and pgAdmin with Docker

```bash
docker-compose up -d
```

Access:
- PostgreSQL: `localhost:5432`
- pgAdmin: [http://localhost:5050](http://localhost:5050)

### 6. Run the ETL Pipeline


The script will:
- Create required tables
- Extract data from the API
- Load it to staging
- Apply SCD2 merge into the dimension table

## Technologies Used

- Python (requests, pandas, SQLAlchemy)
- PostgreSQL 15+ (via Docker)
- pgAdmin4 (via Docker)
- Docker Compose
- SQL DDL and DML (SCD2 with MERGE)
- dotenv

## Sample Output (dim.dim_character)

| character_key | api_id | character_name | episode_count | is_current | effective_date | end_date |
|---------------|--------|----------------|----------------|------------|----------------|----------|
| 1             | 1      | Rick Sanchez   | 51             | true       | 2025-05-10     | NULL     |

## Notes

- PostgreSQL 15+ is required for `MERGE`
- Designed for modular extensibility (e.g., Airflow, dbt, etc.)

## Future Enhancements

- Add logging and error handling
- Build dashboard integration
- Extend for multiple dimensions (e.g., episodes, locations)

## Acknowledgements

- [Rick and Morty API](https://rickandmortyapi.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)