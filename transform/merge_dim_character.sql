-- Step 1: Expire old records (set is_current = false)
UPDATE dim.dim_character d
SET is_current = false,
    end_date = CURRENT_DATE
FROM staging.rick_and_morty_characters s
WHERE d.api_id = s.api_id
  AND d.is_current = true
  AND d.episode_count <> s.no_ep;

-- Step 2: Insert new records
MERGE INTO dim.dim_character d
USING staging.rick_and_morty_characters s
ON d.api_id = s.api_id AND d.is_current = true
WHEN NOT MATCHED THEN
  INSERT (
    api_id,
    character_name,
    episode_count,
    is_current,
    effective_date,
    created_at
  )
  VALUES (
    s.api_id,
    s.name,
    s.no_ep,
    true,
    CURRENT_DATE,
    s.created_at::timestamp
  );
