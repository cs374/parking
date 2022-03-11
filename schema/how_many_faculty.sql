-- looks at how many spaces are occupied in faculty lots by day
-- and shows the number of available spots in the respective faculty lot
DROP FUNCTION IF EXISTS how_many_faculty(g_zone integer, day text);

CREATE FUNCTION how_many_faculty(g_zone integer, day text)
RETURNS TABLE(deck text, time_stamp text, occupied_spaces integer, available_spaces integer) AS $$

 SELECT garage.deck, o.time_stamp, o.occupied, CAST(SUM(garage.spaces - o.occupied) AS integer) AS available 
 FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE garage.zone_id = 2
	OR garage.zone_id = 6
	OR garage.zone_id = 12
	OR garage.zone_id = 27
GROUP BY garage.deck, o.time_stamp, o.occupied
ORDER BY time_stamp, deck

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION how_many_faculty(g_zone integer, day text) OWNER TO parking;