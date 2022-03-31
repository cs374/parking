from flask import Flask, render_template, request, flash, redirect
import psycopg, re

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=baker3cl password=111817139")

def select_garage():
    query = """
        SELECT hour, avg_visitors
        FROM avg_visitors_per_hour(%s)
        ORDER BY hour
        """
    garage_input = request.args.get("garage")
    if garage_input:
        db = return_database()
        current = db.cursor()
        current.execute(query, (garage_input,))
        data=current.fetchall()
    else:
        data=None
    return render_template("avg_visitors_per_hour.html", data=data)
    
