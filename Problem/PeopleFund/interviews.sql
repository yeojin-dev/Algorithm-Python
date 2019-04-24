SET sql_mode = '';
SELECT c1.contest_id, c1.hacker_id, c1.name, SUM(s2.total_submissions) AS sum1, SUM(s2.total_accepted_submissions) AS sum2, SUM(v2.total_views) AS sum3, SUM(v2.total_unique_views) AS sum4 FROM contests AS c1
JOIN colleges AS c2 ON c1.contest_id = c2.contest_id
JOIN challenges AS c3 ON c2.college_id = c3.college_id
LEFT JOIN (
    SELECT v1.challenge_id AS challenge_id, SUM(v1.total_views) AS total_views, SUM(v1.total_unique_views) AS total_unique_views FROM view_stats AS v1 GROUP BY v1.challenge_id
) AS v2 ON c3.challenge_id = v2.challenge_id
LEFT JOIN (
    SELECT s1.challenge_id AS challenge_id, SUM(s1.total_submissions) AS total_submissions, SUM(s1.total_accepted_submissions) AS total_accepted_submissions FROM submission_stats AS s1 GROUP BY s1.challenge_id
) AS s2 ON c3.challenge_id = s2.challenge_id
GROUP BY c1.hacker_id
HAVING sum1 != 0 OR sum2 != 0 OR sum3 != 0 OR sum4 != 0
ORDER BY c1.contest_id;
