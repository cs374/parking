# NOTE: \copy imports from a local file
#       COPY imports from another database
# include echo statements

psql -c "\copy garage FROM garage.csv WITH CSV HEADER" parking


psql -c "\copy occupancy FROM occupancy.csv WITH CSV HEADER" parking


psql -c "\copy class FROM class.csv WITH CSV HEADER" parking
