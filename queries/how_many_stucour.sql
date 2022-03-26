--
-- Determines how many estimated students and courses were on campus at a given term and day.
-- Note: this doesn't consider that one student may be in sequential courses at one time.
--

DROP FUNCTION IF EXISTS how_many_stucour(term integer, day text);

CREATE FUNCTION how_many_stucour(term integer, day text)
RETURNS TABLE(beg_time time, num_students bigint, num_courses bigint) AS $$

    SELECT beg_time, sum(enrolled) AS num_students, count(*) AS num_courses
    FROM enrollment
    WHERE days LIKE CONCAT('%', $2, '%')
        AND term = $1
    GROUP BY beg_time
    HAVING sum(enrolled) > 50 --eliminates times with less than 50 people 
        AND count(*) > 5 --elimates times with less than 5 courses
    ORDER BY beg_time;

$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION how_many_stucour(term integer, day text)OWNER TO parking;



