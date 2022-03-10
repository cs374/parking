"""Running this code will format the postgres output from the stucour.sql 
so the output can be copied and pasted into the html file.
"""

f = open("data.csv", "r")
for x in f:
    str = x[:-1]  # removes new line character
    fcomma = str.index(',')  # first comma
    lcomma = str.rindex(',')  # second comma

    time = str[:fcomma]
    stu = str[fcomma + 1:lcomma]
    cour = str[lcomma + 1:]
    print(f"[{time}, {stu}, {cour}],")
