-- script that lists all the cities of California that 
-- can be found in the database hbtn_0d_usa.
SELECT id, name 
FROM states
WHERE state_id IN 
	(SELECT state_id 
	 	FROM cities
	 	WHERE state_id = 1);
