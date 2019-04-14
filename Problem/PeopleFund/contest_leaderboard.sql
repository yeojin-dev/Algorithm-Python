SELECT h.hacker_id, h.name, s.total_score FROM hackers AS h
JOIN (
    SELECT s2.hacker_id, SUM(s2.max_score) AS total_score FROM (
        SELECT s1.hacker_id, s1.challenge_id, MAX(s1.score) AS max_score FROM submissions AS s1
        GROUP BY s1.hacker_id, s1.challenge_id
    ) AS s2
    GROUP BY s2.hacker_id
) AS s ON s.hacker_id = h.hacker_id AND s.total_score != 0
ORDER BY total_score DESC, h.hacker_id;
