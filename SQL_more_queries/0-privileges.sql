-- Check if user_0d_1 exists before showing grants
SELECT 
  CASE 
    WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') 
    THEN SHOW GRANTS FOR 'user_0d_1'@'localhost'
    ELSE 'There is no such grant defined for user ''user_0d_1'' on host ''localhost'''
  END;

-- Check if user_0d_2 exists before showing grants
SELECT 
  CASE 
    WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost') 
    THEN SHOW GRANTS FOR 'user_0d_2'@'localhost'
    ELSE 'There is no such grant defined for user ''user_0d_2'' on host ''localhost'''
  END;
