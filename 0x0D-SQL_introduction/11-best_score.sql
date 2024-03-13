-- This script lists all records with scores >= 10 in 'second_table' of the database.
-- list the score and name of the person ordered by the highest score.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
