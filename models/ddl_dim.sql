CREATE SCHEMA IF NOT EXISTS dim;

CREATE TABLE IF NOT EXISTS dim.dim_character (
    character_key SERIAL PRIMARY KEY,
    api_id INTEGER,
    character_name TEXT NOT NULL,
    episode_count INTEGER NOT NULL,
    is_current BOOLEAN DEFAULT TRUE,
    effective_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);