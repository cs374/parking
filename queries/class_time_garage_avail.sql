DROP FUNCTION IF EXISTS class_time_garage_avail(start_time text);

CREATE FUNCTION class_time_garage_avail(start_time text) 
RETURNS TABLE(deck text, available_spots integer) AS $$

SELECT ga.deck, CAST(AVG(ga.spaces - o.occupied) AS integer) AS avail 
FROM occupancy AS o
	JOIN garage AS ga ON ga.zone_id = o.zone_id
	JOIN enrollment AS e ON 1 = 1
WHERE o.time_stamp LIKE CONCAT('% ', SUBSTRING($1, 1, 2), ':', CAST((CAST(SUBSTRING($1, 4, 5) AS INT) + 1) AS VARCHAR(20)))
AND   e.beg_time LIKE CONCAT('%',$1, '%')
AND   ga.spaces - o.occupied > 0
GROUP BY ga.deck
ORDER BY avail
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION class_time_garage_avail(start_time text) OWNER TO parking;