-- Creates a table unique_id on the server
-- Doesn't fail if table exists
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
