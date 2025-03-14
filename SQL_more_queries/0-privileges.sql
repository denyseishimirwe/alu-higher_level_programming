-- Check if user_0d_1 exists
SELECT COUNT(*) 
FROM mysql.user 
WHERE user = 'user_0d_1' AND host = 'localhost';

-- Check if user_0d_2 exists
SELECT COUNT(*) 
FROM mysql.user 
WHERE user = 'user_0d_2' AND host = 'localhost';

-- Create user_0d_1 and grant root privileges if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create user_0d_2 and grant specific privileges if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON `user_2_db`.* TO 'user_0d_2'@'localhost';

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
