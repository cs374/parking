--
-- Gets the daily garage occupancy based on the garage and day.
--

DROP FUNCTION IF EXISTS garage_daily_stats(g_zone integer, day date);

CREATE FUNCTION garage_daily_stats(g_zone integer, day date)
RETURNS TABLE(time_stamp timestamp, occ_spaces integer) AS $$

  SELECT time_stamp, occupied
  FROM garage
    JOIN occupancy AS o ON garage.zone_id = o.zone_id
  WHERE garage.zone_id = $1
    AND DATE(o.time_stamp) = day
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION garage_daily_stats(g_zone integer, day date) OWNER TO parking;


