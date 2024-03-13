-- This script lists the number of records with the same score in 'second_table' of the database.
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
