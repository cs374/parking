psql -h data.cs.jmu.edu -c "\copy garage FROM garage.csv WITH CSV HEADER" parking
psql -h data.cs.jmu.edu -c "\copy timestamps FROM timestamps.csv WITH CSV HEADER" parking