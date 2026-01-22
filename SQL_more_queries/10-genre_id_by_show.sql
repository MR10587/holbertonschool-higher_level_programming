-- GENRE ID
SELECT s.title, g.genre_id
FROM tv_shows s
JOIN tv_show_genres g
ORDER BY s.title, g.genre_id;