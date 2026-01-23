-- COUNT 
SELECT g.name AS genre, COUNT(s.genre_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres s
ON g.id = s.genre_id;
WHERE g.genres_name IS NOT NULL
GROUP BY g.id, g.name
ORDER BY COUNT(s.genre_id) DESC;
