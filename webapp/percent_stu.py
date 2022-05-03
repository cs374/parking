from datetime import date
from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app, datetime

def percent_stu_combo():
    hour = request.args.get("hour")
    date = request.args.get("date")
    garage_space_data = get_garage_spaces()
    percent_data, is_input_wrong = select_hour_date(hour, date)
    return render_template('percent_stu.html', data=garage_space_data, percent_data=percent_data, is_input_wrong=is_input_wrong, hour_input=hour, date_input=date)

def get_garage_spaces():
    # Gets each deck with it's corresponding number of spaces

    query = """
    SELECT deck, sum(spaces) 
    FROM garage
    GROUP BY deck
    ORDER BY deck;
    """
    db = app.return_database()
    current = db.cursor()
    current.execute(query,)
    data=current.fetchall()
    return data

def select_hour_date(hour_input, date_input):
    # Executes the logic for getting the percentage_occupied data

    query = """
    SELECT deck, avg_occupied
	FROM percentage_occupied(%s, %s);
    """

    is_input_wrong = None
    if hour_input and date_input:
        if re.match('^[0-9][0-9]$', hour_input) and int(hour_input) < 24:
            db = app.return_database()
            current = db.cursor()
            current.execute(query, (hour_input, date_input,))
            data=current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return data, is_input_wrong
    else:
        data=None
        hour_input='10'
        date_input="2021-02-17"

    return data, is_input_wrong