SELECT t1.submission_date, t1.hacker_cnt, t2.hacker_id, h.name
-- 매일 제출한 hacker_id의 개수 찾기
FROM (
    SELECT p1.submission_date, COUNT(DISTINCT p1.hacker_id) AS hacker_cnt
    FROM (
        SELECT submission_date, hacker_id, @hacker_rank := CASE WHEN @hacker_group != hacker_id THEN 1 ELSE @hacker_rank + 1 END AS hacker_rank, @hacker_group := hacker_id
        FROM (
            SELECT DISTINCT submission_date, hacker_id FROM submissions
            ORDER BY hacker_id, submission_date
        ) AS a,
        (
            SELECT @hacker_rank := 1, @hacker_group := 0
        ) AS t
    ) AS p1
    JOIN (
        SELECT submission_date, @date_rank := @date_rank + 1 AS date_rank
        FROM (
            SELECT DISTINCT submission_date FROM submissions ORDER BY submission_date
        ) AS b,
        (
            SELECT @date_rank := 0
        ) AS r
    ) AS p2
    ON p1.submission_date = p2.submission_date AND hacker_rank = date_rank
    GROUP BY p1.submission_date
) AS t1
-- 가장 많은 제출을 한 사람 찾기
JOIN (
    SELECT submission_date, hacker_id, sub_count, @s_rank := CASE WHEN @d_group != submission_date THEN 1 ELSE @s_rank + 1 END AS max_rank, @d_group := submission_date
    FROM (
        SELECT submission_date, hacker_id, COUNT(*) AS sub_count
        FROM submissions AS s
        GROUP BY submission_date, hacker_id
        ORDER BY submission_date, sub_count DESC, hacker_id
    ) AS c,
    (
        SELECT @s_rank := 1, @d_group := 0
    ) AS r
) AS t2
ON t1.submission_date = t2.submission_date AND max_rank = 1
JOIN hackers AS h ON h.hacker_id = t2.hacker_id
ORDER BY t1.submission_date;
