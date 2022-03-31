from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app

def select_garage():
    query = """
        SELECT hour, avg_visitors
        FROM avg_visitors_per_hour(%s)
        ORDER BY hour
        """
    garage_input = request.args.get("garage")
    if garage_input:
        db = app.return_database()
        current = db.cursor()
        current.execute(query, (garage_input,))
        data=current.fetchall()
    else:
        data=None
        garage=None
    return render_template("avg_visitors_per_hour.html", data=data, garage_input=garage_input)
    
