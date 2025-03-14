-- Create users if they don't exist

CREATE USER 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
