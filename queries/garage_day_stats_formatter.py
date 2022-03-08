"""Running this code will format the postgres output from the garage_day_stats.sql 
so the output can be copied and pasted into the html file.
"""

f = open("data.csv", "r")
for x in f:
    str = x[:-1]  # removes new line character
    quote = str.index(',')
    date = str[quote-6:quote]
    spaces = str[quote + 1:]
    print(f"[\"{date}, {spaces}], ")
