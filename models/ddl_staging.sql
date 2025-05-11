CREATE SCHEMA IF NOT EXISTS staging;

CREATE TABLE IF NOT EXISTS staging.rick_and_morty_characters (
    api_id INTEGER,
    name TEXT,
    no_ep INTEGER,
    created_at TIMESTAMP
);