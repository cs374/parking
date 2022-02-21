DROP TABLE IF EXISTS garage;

CREATE TABLE garage (
	zone_id integer NOT NULL,
	num_spaces integer NOT NULL,
	deck text NOT NULL,
	used_by text NOT NULL
);

COMMENT ON TABLE garage IS 'Parking garages at JMU';

DROP TABLE IF EXISTS timestamps;

CREATE TABLE timestamps (
	zone_id integer NOT NULL,
	time text NOT NULL,
	occupied integer NOT NULL,
	visitor integer NOT NULL
);

COMMENT ON TABLE timestamps IS 'Timestamps for parking at JMU'