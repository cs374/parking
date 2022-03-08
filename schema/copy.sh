# NOTE: \copy imports from a local file
#       COPY imports from another database

echo \copy garage FROM csv
psql -c "\copy garage FROM garage.csv WITH CSV HEADER" parking

echo \copy occupancy FROM csv
psql -c "\copy occupancy FROM occupancy.csv WITH CSV HEADER" parking

echo \copy class FROM csv
psql -c "\copy class FROM class.csv WITH CSV HEADER" parking

echo COPY enrollment FROM jmudb
psql -c "COPY (
	SELECT DISTINCT
	  term, nbr, subject, number, title, section, days, beg_time, end_time, enrolled
	FROM enrollment
	WHERE term >= 1211 -- Spring 2021
	  AND term <= 1218 -- Fall 2021
	  AND enrolled > 0
	  AND days IS NOT NULL
	  AND room IS NOT NULL
	ORDER BY subject, number
  ) TO STDOUT;" jmudb | \
  psql -c "COPY enrollment FROM STDIN;" parking
