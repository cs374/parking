--
-- Gets the daily garage occupancy based on the garage and day.
--

DROP FUNCTION IF EXISTS garage_daily_stats(g_zone integer, day text);

CREATE FUNCTION garage_daily_stats(g_zone integer, day text)
RETURNS TABLE(g_name text, occ_spaces integer) AS $$

  SELECT time_stamp, occupied
  FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE garage.zone_id = $1
    AND o.time_stamp LIKE $2 --just need to figure out the LIKE % formatting here

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION garage_daily_stats(g_zone integer, day timestamp) OWNER TO parking;


