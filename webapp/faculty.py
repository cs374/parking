from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app

query = """
SELECT deck, occupied_spaces, available_spaces
	FROM faculty(%s, %s, %s);
"""

def availableSpots():
    is_input_wrong = None
    hour_input = request.args.get("hour")
    garage_input = request.args.get("garage")
    if hour_input:
        if re.match('^[0-9][0-9]$', hour_input):
            db = app.return_database()
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

    