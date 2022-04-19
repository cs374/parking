from datetime import date
from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app, datetime, time

app = Flask(__name__)
app.secret_key = "key"

query = """
    SELECT deck, avg_occupied
	FROM percentage_occupied(%s, %s);
"""

def select_hour_date():
    is_input_wrong = None

    # Gets the current hour, month, and date in the correct format
    now = datetime.datetime.now()
    hour_input = str(now.hour)
    
    if date.today().month > 9:
        month = str(date.today().month)
    else:
        month = "0" + str(date.today().month)

    if date.today().day > 9:
        day = str(date.today().day)
    else:
        day = "0" + str(date.today().day)

    date_input ="2021-" + month + "-" + day
    
    # Connects to Database and Executes Query 
    db = psycopg.connect("host=localhost dbname=parking user=parking password=JUvWSJ2hgRp93TmU")
    current = db.cursor()
    current.execute(query, (hour_input, date_input))
    data=current.fetchall()

    return render_template("index.html", data=data, hour_input=hour_input, date_input=date_input)
