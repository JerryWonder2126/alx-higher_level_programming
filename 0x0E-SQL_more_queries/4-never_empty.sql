-- Creates a table id_not_null on the server
-- Doesn't fail if table exists
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
