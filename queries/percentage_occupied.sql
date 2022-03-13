/*This function returns the average number of occupied spaces on a specific date and hour*/
DROP FUNCTION IF EXISTS percentage_occupied(hour text, date text);

CREATE FUNCTION percentage_occupied(hour text, date text)
RETURNS TABLE(deck text, hour text, avg_occupied bigint) AS $$

SELECT g.deck, SUBSTRING(time_stamp, 12, 2) AS hour, sum(occupied)/12 AS avg_occupied
FROM garage AS g 
	JOIN occupancy AS o ON g.zone_id = o.zone_id
WHERE SUBSTRING(time_stamp, 12, 2) = $1
	AND SUBSTRING(time_stamp, 0, 11) = $2
GROUP BY g.deck, SUBSTRING(time_stamp, 12, 2)
;
	
$$ LANGUAGE SQL STABLE STRICT;
ALTER FUNCTION percentage_occupied(hour text, date text) OWNER TO parking;