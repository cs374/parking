from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app

query = """
SELECT deck, avg_occupied, avg_available
	FROM faculty(%s, %s, %s);
"""

def availableSpots():
    is_input_wrong = None
    hour_input = request.args.get("hour")
    garage_input = request.args.get("garage")
    date_input = request.args.get("date")
    if hour_input:
        if re.match('^[0-9][0-9]$', hour_input) and int(hour_input) < 24 and re.match('^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$', date_input):
            db = app.return_database()
            current = db.cursor()
            current.execute(query, (garage_input, hour_input, date_input))
            data = current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return render_template("faculty.html", data=data, is_input_wrong=is_input_wrong)
    else:
        data=None
        hour_input="10"
        date_input="2021-02-17"
    return render_template("faculty.html", hour_input=hour_input, date_input=date_input, garage_input=garage_input,
                            data=data, is_input_wrong=is_input_wrong)

    