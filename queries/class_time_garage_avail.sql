--This will show you the number of parking spots available at 
--each garage at a given time (which is the parameter). 
DROP FUNCTION IF EXISTS class_time_garage_avail(start_time time);

CREATE FUNCTION class_time_garage_avail(start_time time) 
RETURNS TABLE(deck text, available_spots integer) AS $$

SELECT ga.deck, CAST(AVG(ga.spaces - o.occupied) AS integer) AS avail 
FROM occupancy AS o
	JOIN garage AS ga ON ga.zone_id = o.zone_id
	JOIN enrollment AS e ON 1 = 1

WHERE CASE WHEN (CAST(start_time AS time) < '00:10') OR (CAST(start_time AS time) > '11:50') THEN

	CAST(o.time_stamp AS time) = '00:15'
	
ELSE
	CAST(o.time_stamp AS time) < (CAST(start_time AS time) + interval '10 minutes')
	AND CAST(o.time_stamp AS time) > (CAST(start_time AS time) - interval '10 minutes')
	
END

AND EXTRACT(MONTH FROM o.time_stamp) < 9
AND EXTRACT(MONTH FROM o.time_stamp) > 5

-- AND CAST(e.beg_time AS time) < CAST(start_time AS time) + interval '30 minutes'
-- AND CAST(e.beg_time AS time) > CAST(start_time AS time) - interval '30 minutes'

AND   ga.spaces - o.occupied > 0

GROUP BY ga.deck
ORDER BY avail
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION class_time_garage_avail(start_time time) OWNER TO parking;