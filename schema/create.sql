
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
	time_stamp text NOT NULL,
	zone_id integer NOT NULL,
	occupied integer NOT NULL,
	visitor integer NOT NULL
);

ALTER TABLE occupancy OWNER TO parking;

COMMENT ON TABLE occupancy IS 'occupancy for parking at JMU';


DROP TABLE IF EXISTS class;

CREATE TABLE class (
	day text NOT NULL,
	start_time text NOT NULL,
	end_time text NOT NULL,
	zone_id integer NOT NULL,
	term text NOT NULL
);

ALTER TABLE class OWNER TO parking;

COMMENT ON TABLE class IS 'Class Meeting Times at JMU';



