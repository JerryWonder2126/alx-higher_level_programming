-- Creates a table force_name on the server
-- Doesn't fail if table exists
CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256)
);
