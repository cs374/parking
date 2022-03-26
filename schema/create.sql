
DROP TABLE IF EXISTS garage CASCADE;

CREATE TABLE garage (
	zone_id integer NOT NULL,
	deck text NOT NULL,
	zone text NOT NULL,
	spaces integer NOT NULL
);
ALTER TABLE garage OWNER TO parking;

COMMENT ON TABLE garage IS 'Parking garages at JMU';


DROP TABLE IF EXISTS occupancy;

CREATE TABLE occupancy (
	time_stamp timestamp NOT NULL,
	zone_id integer NOT NULL,
	occupied integer NOT NULL,
	visitor integer NOT NULL
);

ALTER TABLE occupancy OWNER TO parking;

COMMENT ON TABLE occupancy IS 'Occupancy for parking at JMU';


DROP TABLE IF EXISTS class;

CREATE TABLE class (
	day text NOT NULL,
	start_time time NOT NULL,
	end_time time NOT NULL,
	zone_id integer NOT NULL,
	term text NOT NULL
);

ALTER TABLE class OWNER TO parking;

COMMENT ON TABLE class IS 'Class Meeting Times at JMU';


DROP TABLE IF EXISTS enrollment;

CREATE TABLE enrollment (
	term integer NOT NULL,
	nbr integer NOT NULL,
	subject text NOT NULL,
	number integer NOT NULL,
	title text NOT NULL,
	section text NOT NULL,
	days text NOT NULL,
	beg_time time,
	end_time time,
	enrolled integer NOT NULL
);

ALTER TABLE enrollment OWNER TO parking;

COMMENT ON TABLE enrollment IS 'Enrollment data at JMU';
