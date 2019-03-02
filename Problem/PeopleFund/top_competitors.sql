SELECT hackers.hacker_id, hackers.name FROM submissions
JOIN challenges ON submissions.challenge_id = challenges.challenge_id
JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
JOIN hackers ON submissions.hacker_id = hackers.hacker_id
WHERE submissions.score = difficulty.score
    AND challenges.difficulty_level = difficulty.difficulty_level
GROUP BY hackers.hacker_id, hackers.name
HAVING COUNT(submissions.hacker_id) > 1
ORDER BY COUNT(submissions.hacker_id) DESC, submissions.hacker_id ASC;
