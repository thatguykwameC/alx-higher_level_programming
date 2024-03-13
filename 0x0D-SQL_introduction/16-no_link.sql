-- This script lists all records in 'second_table of the database whose 'name' field is not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
