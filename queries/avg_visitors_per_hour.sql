/*This function returns the average number of visitor per hour for a inputted deck */
DROP FUNCTION IF EXISTS avg_visitors_per_hour(g_name text);

CREATE FUNCTION avg_visitors_per_hour(g_name text)
RETURNS TABLE(deck text, hour text, avg_visitors bigint) AS $$


SELECT DISTINCT deck, SUBSTRING(o.time_stamp,12,2), 
	   SUM(o.visitor)/COUNT(DISTINCT SUBSTRING(o.time_stamp,0,11)) AS avg_vistiors
FROM garage AS g
	JOIN occupancy AS o ON g.zone_id = o.zone_id
WHERE g.deck = $1
GROUP BY deck, SUBSTRING(o.time_stamp,12,2)
ORDER BY SUBSTRING(o.time_stamp,12, 2)
	
$$ LANGUAGE SQL STABLE STRICT;
ALTER FUNCTION avg_visitors_per_hour(g_name text) OWNER TO parking;