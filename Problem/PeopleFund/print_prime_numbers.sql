SELECT GROUP_CONCAT(prime SEPARATOR '&') FROM (
    SELECT @num := @num + 1 AS prime FROM information_schema.tables AS t1, information_schema.tables AS t2, (SELECT @num := 1) AS temp
) AS temp_prime
WHERE prime <= 1000
AND NOT EXISTS (
    SELECT * FROM (
        SELECT @num1 := @num1 + 1 as divisor FROM information_schema.tables AS t3, information_schema.tables AS t4, (SELECT @num1 := 1) AS temp1 LIMIT 1000
    ) AS temp2
    WHERE MOD(prime, divisor) = 0 AND prime != divisor
);
