-- looks at how many spaces are occupied in faculty lots by day
-- and shows the number of available spots in the respective faculty lot
DROP FUNCTION IF EXISTS faculty(deck text, hour text, day text);

CREATE FUNCTION faculty(deck text, hour text, day text)
RETURNS TABLE(deck text, avg_occupied integer, avg_available integer) AS $$

 SELECT garage.deck,
 	ROUND(AVG(o.occupied))::int AS avg_occupied, 
	ROUND(AVG(garage.spaces - o.occupied))::int AS avg_available 
 FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE (garage.zone_id = 2 
    OR garage.zone_id = 6 
    OR garage.zone_id = 12 
    OR garage.zone_id = 27)
	AND garage.deck = $1
    AND SUBSTRING(time_stamp::text, 12, 2) = $2
    AND SUBSTRING(time_stamp::text, 0, 11) = $3
GROUP BY garage.deck
ORDER BY garage.deck

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION faculty(deck text, hour text, day text) OWNER TO parking;