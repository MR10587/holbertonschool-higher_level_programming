-- COUNT 
SELECT tv_genres.name g AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM g
LEFT JOIN tv_show_genres s
ON g.id = s.genre_id;
WHERE g.genres_name IS NOT NULL
ORDER BY COUNT(s.genre_id) DESC;
