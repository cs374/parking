DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS timestamps;
DROP TABLE IF EXISTS garage;

CREATE TABLE garage (
	zone_id integer NOT NULL,
	deck text NOT NULL,
	zone text NOT NULL,
	spaces integer NOT NULL
);
ALTER TABLE garage OWNER TO parking;

COMMENT ON TABLE garage IS 'Parking garages at JMU';

DROP TABLE IF EXISTS timestamps;

CREATE TABLE timestamps (
	time_stamp text NOT NULL,
	zone_id integer NOT NULL,
	occupied integer NOT NULL,
	visitor integer NOT NULL
);

ALTER TABLE timestamps OWNER TO parking;

COMMENT ON TABLE timestamps IS 'Timestamps for parking at JMU';

DROP TABLE IF EXISTS classes;

CREATE TABLE classes (
	day text NOT NULL,
	start_time text NOT NULL,
	end_time text NOT NULL,
	zone_id integer NOT NULL
);

ALTER TABLE timestamps OWNER TO parking;

COMMENT ON TABLE timestamps IS 'Class Meeting Times at JMU';