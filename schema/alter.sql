/* set primary key for garage table as zone id */
ALTER TABLE garage ADD PRIMARY KEY (zone_id);

/* set primary key for occupancy table as zone id*/
ALTER TABLE occupancy ADD PRIMARY KEY (time_stamp, zone_id);

/* set foreign key for occupancy table as the zone_id from garage table */
ALTER TABLE occupancy ADD FOREIGN KEY (zone_id) REFERENCES garage;

/* set primary key for classes table as (start_time, end_time, and day) */
ALTER TABLE classes ADD PRIMARY KEY (zone_id, start_time, end_time, day);

/* set foreign key for classes table as zone_id 
ALTER TABLE classes ADD FOREIGN KEY (zone_id) REFERENCES garage; */

ALTER TABLE classes ADD FOREIGN KEY (zone_id) REFERENCES garage;



