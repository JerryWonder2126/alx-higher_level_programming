-- Select all values with name not null
SELECT score, `name` FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
