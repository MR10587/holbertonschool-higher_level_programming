-- COUNT SHOWS
SELECT g.name AS genre, COUNT(s.genre_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres s
ON g.id = s.genre_id
WHERE COUNT(s.genre_id) IS NOT 0
GROUP BY g.id, g.name
ORDER BY number_of_shows DESC;
