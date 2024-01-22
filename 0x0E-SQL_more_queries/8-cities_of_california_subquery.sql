-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT s.id, c.name
FROM states s INNER JOIN cities c
ON c.state_id = s.id
ORDER BY name ASC
