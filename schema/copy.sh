# NOTE: \copy imports from a local file
#       COPY imports from another database

echo \copy garage FROM csv
psql -c "\copy garage FROM garage.csv WITH CSV HEADER" parking

echo \copy occupancy FROM csv
psql -c "\copy occupancy FROM occupancy.csv WITH CSV HEADER" parking

echo \copy class FROM csv
psql -c "\copy class FROM class.csv WITH CSV HEADER" parking
