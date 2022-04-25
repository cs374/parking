from datetime import date
from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app, datetime

query = """
    SELECT deck, avg_occupied
	FROM percentage_occupied(%s, %s);
"""

def select_hour_date():
    is_input_wrong = None
    hour_input = request.args.get("hour")
    date_input = request.args.get("date")
    if hour_input and date_input:
        if re.match('^[0-9][0-9]$', hour_input) and int(hour_input) < 24:
            db = app.return_database()
            current = db.cursor()
            current.execute(query, (hour_input, date_input,))
            data=current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return render_template("percentage_occupied.html", data=data, is_input_wrong=is_input_wrong)
    else:
        data=None
        hour_input='10'
        date_input="2021-02-17"
    return render_template("percentage_occupied.html", data=data, is_input_wrong=is_input_wrong, hour_input=hour_input, date_input=date_input)

    