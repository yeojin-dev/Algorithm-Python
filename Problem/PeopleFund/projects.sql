SET sql_mode = '';
SELECT start_date, end_date
FROM (SELECT start_date FROM projects WHERE start_date NOT IN (SELECT end_date FROM projects)) AS a,
(SELECT end_date FROM projects WHERE end_date NOT IN (SELECT start_date FROM projects)) AS b
WHERE start_date < end_date
GROUP BY start_date
ORDER BY DATEDIFF(end_date, start_date), start_date;
