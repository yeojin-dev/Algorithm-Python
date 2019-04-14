SELECT h.hacker_id, h.name, COUNT(h.name) AS c_count FROM hackers AS h
JOIN challenges AS c ON h.hacker_id = c.hacker_id
GROUP BY c.hacker_id, h.name
HAVING c_count = (
    SELECT MAX(c1.h_count) FROM (
        SELECT COUNT(hacker_id) AS h_count FROM challenges
        GROUP BY hacker_id
        ORDER BY hacker_Id
    ) AS c1
)
OR c_count IN (
    SELECT c2.total_count FROM (
        SELECT COUNT(*) AS total_count FROM challenges
        GROUP BY hacker_id
    ) AS c2
    GROUP BY c2.total_count
    HAVING COUNT(c2.total_count) = 1
)
ORDER BY c_count DESC, c.hacker_id;
