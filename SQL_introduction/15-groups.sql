-- QROUPS
SELECT score, COUNT(score)
FROM second_table
GROUP BY score
ORDER BY SCORE DESC;
