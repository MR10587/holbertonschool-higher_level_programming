-- NO GENRE
SELECT s.title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ORDER BY s.title, g.genre_id;
