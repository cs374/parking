ALTER TABLE garage ADD PRIMARY KEY (zone_id);

ALTER TABLE timestamps ADD PRIMARY KEY (zone_id)
ALTER TABLE timestamps ADD FOREIGN KEY (zone_id) REFERENCES garage;
ALTER TABLE timestamps ADD PRIMARY KEY (timestamp)


ALTER TABLE classes ADD FOREIGN KEY (zone_id) REFERENCES garage;
ALTER TABLE classes ADD PRIMARY KEY (start_time);
ALTER TABLE classes ADD PRIMARY KEY (end_time);


