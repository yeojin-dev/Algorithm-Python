SELECT (salary * months) as earning, count(*) FROM employee GROUP BY 1 ORDER BY earning DESC LIMIT 1;
