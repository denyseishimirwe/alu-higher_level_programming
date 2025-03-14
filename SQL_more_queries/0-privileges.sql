-- Create users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant root privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Grant specific privileges to user_0d_2 on user_2_db
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Show grants for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

