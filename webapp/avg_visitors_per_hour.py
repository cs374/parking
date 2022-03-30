from flask import Flask, render_template, request, flash, redirect
import psycopg, re

app = Flask(__name__)
app.secret_key = "key"

query = """
    SELECT hour, avg_visitors
	FROM avg_visitors_per_hour(%s)
	ORDER BY hour
"""

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=baker3cl password=111817139")

@app.route('/')
def select_garage():
    garage_input = request.args.get("garage")
    if garage_input:
        db = return_database()
        current = db.cursor()
        current.execute(query, (garage_input,))
        data=current.fetchall()
    else:
        data=None
    return render_template("avg_visitors_per_hour.html", data=data)
    
