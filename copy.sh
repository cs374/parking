psql -c "\copy garage FROM garage.csv WITH CSV HEADER" parking
psql -c "\copy timestamps FROM timestamps.csv WITH CSV HEADER" parking
psql -c "\copy classes FROM classes.csv WITH CSV HEADER" parking
