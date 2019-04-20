SELECT s2.name FROM (
    SELECT s1.name, p1.salary, p2.salary AS friend_salary FROM students AS s1
    JOIN friends AS f ON f.id = s1.id
    JOIN packages AS p1 ON p1.id = s1.id
    JOIN packages AS p2 ON p2.id = f.friend_id
) AS s2
WHERE s2.salary < friend_salary
ORDER BY friend_salary;
