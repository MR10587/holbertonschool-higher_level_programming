-- CITIES OF CALIFORNIA
SELECT * FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name='California'
);
