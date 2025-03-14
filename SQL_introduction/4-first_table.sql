-- This script creates the table 'first_table' in the current database
-- If the table already exists, it will not cause an error

CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
