SELECT w.id, p.age, w.coins_needed, w.power FROM wands AS w
JOIN wands_property AS p ON w.code = p.code
WHERE w.coins_needed = (
    SELECT min(coins_needed) FROM wands AS w1
    JOIN wands_property AS p1 ON w1.code = p1.code
    WHERE w1.power = w.power AND p1.age = p.age
)
AND p.is_evil = 0
ORDER BY w.power DESC, p.age DESC;
