from flask import Flask, render_template, request, flash, redirect
import psycopg, re

query = """
SELECT deck, occupied_spaces, available_spaces
	FROM faculty(%s, %s, %s);
"""

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=baileyga password=111333868")

def availableSpots():
    is_input_wrong = None
    hour_input = request.args.get("hour")
    garage_input = request.args.get("garage")
    if hour_input:
        if re.match('^[0-9][0-9]$', hour_input):
            db = return_database()
            current = db.cursor()
            current.execute(query, (garage_input, hour_input))
            data=current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return render_template("faculty.html", data=data, is_input_wrong=is_input_wrong)
    else:
        data=None
    return render_template("faculty.html", data=data, is_input_wrong=is_input_wrong)

    