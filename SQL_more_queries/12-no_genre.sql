-- NO GENRE
SELECT s.title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON g.genre_id IS Null
ORDER BY s.title, g.genre_id;
