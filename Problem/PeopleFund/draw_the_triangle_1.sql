SET @num = 21;
SELECT REPEAT('* ', @num := @num - 1) FROM information_schema.tables LIMIT 20; 
