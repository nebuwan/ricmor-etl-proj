CREATE SCHEMA IF NOT EXISTS stage;

CREATE TABLE IF NOT EXISTS stage.rm_characters (
    api_id INTEGER,
    name TEXT,
    no_ep INTEGER,
    created_at TIMESTAMP
);