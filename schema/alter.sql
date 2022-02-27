/* set primary key for garage table as zone id */
ALTER TABLE garage ADD PRIMARY KEY (zone_id);

/* set primary key for occupancy table as zone id*/
ALTER TABLE occupancy ADD PRIMARY KEY (time_stamp, zone_id);

/* set foreign key for occupancy table as the zone_id from garage table */
ALTER TABLE occupancy ADD FOREIGN KEY (zone_id) REFERENCES garage;

/* set primary key for class table as (start_time, end_time, and day) */
ALTER TABLE class ADD PRIMARY KEY (zone_id, start_time, end_time, day);

/* set foreign key for class table as zone_id*/

ALTER TABLE class ADD FOREIGN KEY (zone_id) REFERENCES garage;



