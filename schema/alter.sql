ALTER TABLE garage ADD PRIMARY KEY (zone_id);

ALTER TABLE occupancy ADD PRIMARY KEY (zone_id, time_stamp);
ALTER TABLE occupancy ADD FOREIGN KEY (zone_id) REFERENCES garage;


ALTER TABLE classes ADD FOREIGN KEY (zone_id) REFERENCES garage;
ALTER TABLE classes ADD PRIMARY KEY (zone_id, start_time, end_time, day);
--ALTER TABLE classes ADD PRIMARY KEY (end_time);

--hi


