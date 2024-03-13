-- a script that lists all records of the table second_table
-- does not list rows without a name value
-- lists records by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
