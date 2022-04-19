from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app

def select_garage():
    query = """
        SELECT hour, visitors
        FROM visitors_per_hour(%s, %s)
        """
    garage_input = request.args.get("garage")
    date_input = request.args.get("date")
    if garage_input and date_input:
        db = app.return_database()
        current = db.cursor()
        current.execute(query, (garage_input, date_input))
        data=current.fetchall()
    else:
        data=None
        garage_input="Grace"
        date_input="2021-02-17"
    return render_template("visitors_per_hour.html", data=data, garage_input=garage_input, date_input=date_input)
    
