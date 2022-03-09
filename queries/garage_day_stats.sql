--
-- Gets the daily garage occupancy based on the garage and day.
--

DROP FUNCTION IF EXISTS garage_daily_stats(g_zone integer, day text);

CREATE FUNCTION garage_daily_stats(g_zone integer, day text)
RETURNS TABLE(time_stamp text, occ_spaces integer) AS $$

  SELECT time_stamp, occupied
  FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE garage.zone_id = $1
    AND o.time_stamp LIKE '%' + $2 + '%'
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION garage_daily_stats(g_zone integer, day text) OWNER TO parking;


