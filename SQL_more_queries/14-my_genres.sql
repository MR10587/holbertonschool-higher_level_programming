-- MY GENRES
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_shows
ON tv_shows.name = 'Dexter' 
ORDER BY tv_genres.name;
