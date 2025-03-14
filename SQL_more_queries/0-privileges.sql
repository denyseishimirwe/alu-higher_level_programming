-- Check for user_0d_1
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') 
        THEN CONCAT('Grants for user_0d_1@localhost') 
        ELSE 'There is no such grant defined for user ''user_0d_1'' on host ''localhost''' 
    END AS User_Grants;

SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check for user_0d_2
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost') 
        THEN CONCAT('Grants for user_0d_2@localhost') 
        ELSE 'There is no such grant defined for user ''user_0d_2'' on host ''localhost''' 
    END AS User_Grants;

SHOW GRANTS FOR 'user_0d_2'@'localhost';
