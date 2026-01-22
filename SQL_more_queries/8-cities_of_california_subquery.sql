-- CITIES OF CALIFORNIA
SELECT * FROM cities
WHERE states.id = (
    SELECT id
    FROM cities
    WHERE name='California'
);
