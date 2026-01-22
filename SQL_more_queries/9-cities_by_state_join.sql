-- CITIES BY STATE JOIN
SELECT cities.id, cities.name 
FROM cities
JOIN states
ON states.id = cities.id;
