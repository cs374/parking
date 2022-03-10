/*This function returns the average number of visitor per hour for a inputted deck */
DROP FUNCTION IF EXISTS avg_visitors_per_hour(g_name text);

CREATE FUNCTION avg_visitors_per_hour(g_name text)
RETURNS TABLE(deck text, hour text, avg_visitors numeric) AS $$


SELECT DISTINCT deck, SUBSTRING(o.time_stamp,12,2), AVG(o.visitor)
FROM garage AS g
	JOIN occupancy AS o ON g.zone_id = o.zone_id
WHERE g.deck = $1
	AND NOT SUBSTRING(o.time_stamp,6,2) = '05'
	AND NOT SUBSTRING(o.time_stamp,6,2) = '06'
	AND NOT SUBSTRING(o.time_stamp,6,2) = '07'
	AND NOT SUBSTRING(o.time_stamp,6,2) = '08'
GROUP BY deck, SUBSTRING(o.time_stamp,12,2)
ORDER BY SUBSTRING(o.time_stamp,12, 2)
	
$$ LANGUAGE SQL STABLE STRICT;
ALTER FUNCTION avg_visitors_per_hour(g_name text) OWNER TO parking;