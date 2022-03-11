DROP FUNCTION IF EXISTS how_many_faculty(g_zone integer, day text);

CREATE FUNCTION how_many_faculty(g_zone integer, day text)
RETURNS TABLE(deck text, time_stamp text, occupied_spaces integer) AS $$

  SELECT deck, time_stamp, occupied
  FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE garage.zone_id = 2
	OR garage.zone_id = 6
	OR garage.zone_id = 12
	OR garage.zone_id = 27
	ORDER BY time_stamp, deck

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION how_many_faculty(g_zone integer, day text) OWNER TO parking;