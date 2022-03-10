--
-- Determines how many estimated students and courses were on campus at a given term, day, and time.
-- Note, if looking at a range in the future, this doesn't consider that one student 
-- may be in sequential courses at one time.
--
-- day and start_time won't be text once we figure out the timestamp issues
--

DROP FUNCTION IF EXISTS how_many_stucour(term integer, day text, start_time text);

CREATE FUNCTION how_many_stucour(term integer, day text, start_time text)
RETURNS TABLE(days text, num_students bigint, num_courses bigint) AS $$

    SELECT days, sum(enrolled) AS num_students, count(*) AS num_courses
    FROM enrollment
    WHERE days LIKE CONCAT('%', $2, '%')
	AND term = $1
	AND beg_time LIKE CONCAT('%', $3, '%')
    GROUP BY days
$$ LANGUAGE SQL STABLE STRICT;

ALTER FUNCTION how_many_stucour(term integer, day text, start_time text)OWNER TO parking;



