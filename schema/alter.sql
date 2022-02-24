ALTER TABLE garage ADD PRIMARY KEY (zone_id);

ALTER TABLE occupancy ADD PRIMARY KEY (zone_id);
ALTER TABLE occupancy ADD FOREIGN KEY (zone_id) REFERENCES garage;


ALTER TABLE classes ADD FOREIGN KEY (zone_id) REFERENCES garage;
ALTER TABLE classes ADD PRIMARY KEY (start_time, end_time, day);


