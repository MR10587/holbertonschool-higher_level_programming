-- CITIES OF CALIFORNIA
SELECT * FROM cities
WHERE states_id = (
    SELECT id
    FROM cities
    WHERE name='California'
);
