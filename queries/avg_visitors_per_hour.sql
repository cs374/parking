/*This function returns the average number of visitor per hour for a inputted deck */
DROP FUNCTION IF EXISTS avg_visitors_per_hour(g_name text);

CREATE FUNCTION avg_visitors_per_hour(g_name text)
RETURNS TABLE(date_part double precision, deck text, hour text, avg_visitors bigint) AS $$

SELECT DISTINCT EXTRACT(HOUR FROM o.time_stamp), deck, 
	   CONCAT((EXTRACT(HOUR FROM o.time_stamp))::text, ':00') AS hour,
	   SUM(o.visitor)/COUNT(DISTINCT(o.time_stamp::DATE)) AS avg_vistiors
FROM garage AS g
	JOIN occupancy AS o ON g.zone_id = o.zone_id
WHERE g.deck = $1
GROUP BY deck, EXTRACT(HOUR FROM o.time_stamp)
ORDER BY EXTRACT(HOUR FROM o.time_stamp);
	
$$ LANGUAGE SQL STABLE STRICT;
ALTER FUNCTION avg_visitors_per_hour(g_name text) OWNER TO parking;