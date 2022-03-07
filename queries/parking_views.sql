/*This function returns garages with at least parameter number of spaces*/
DROP FUNCTION IF EXISTS which_garages(num_spaces integer);

CREATE FUNCTION which_garages(num_spaces integer)
RETURNS TABLE(garage_name text, zone_name text) AS $$

SELECT deck, zone
FROM garage AS g
WHERE g.spaces >= $1

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION which_garages (num_spaces integer) OWNER TO parking;

