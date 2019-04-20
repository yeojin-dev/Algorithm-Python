SELECT DISTINCT f1.x, f1.y FROM functions AS f1
JOIN functions AS f2 ON f1.x = f2.y AND f2.x = f1.y
WHERE f1.x NOT IN (
    SELECT f3.x FROM functions AS f3
    WHERE f3.x = f3.y
    GROUP BY f3.x
    HAVING COUNT(*) = 1
)
OR f1.x < f1.y
ORDER BY f1.x;
