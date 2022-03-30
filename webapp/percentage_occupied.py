from flask import Flask, render_template, request, flash, redirect
import psycopg, re

app = Flask(__name__)
app.secret_key = "key"

query = """
SELECT deck, avg_occupied
	FROM percentage_occupied(%s, %s);
"""

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=baker3cl password=111817139")

@app.route('/')
def select_hour_date():
    is_input_wrong = None
    hour_input = request.args.get("hour")
    date_input = request.args.get("date")
    if hour_input and date_input:
        if re.match('^[0-9][0-9]$', hour_input) and re.match('^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$', date_input):
            db = return_database()
            current = db.cursor()
            current.execute(query, (hour_input, date_input,))
            data=current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return render_template("percentage_occupied.html", data=data, is_input_wrong=is_input_wrong)
    else:
        data=None
    return render_template("percentage_occupied.html", data=data, is_input_wrong=is_input_wrong)

    