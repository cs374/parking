from flask import Flask, render_template, request, flash, redirect
import psycopg

app = Flask(__name__)
app.secret_key = "my_key"

query = """
SELECT * FROM class_time_garage_avail(%s)
"""

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=tranaa password=112099828")

@app.route('/')
def select_class_time():
    time_input = request.args.get("time_input", "")
    if time_input:
        db = return_database()
        current = db.cursor()
        current.execute(query, (time_input,))
        data=current.fetchall()
        print(data)
    else:
        data = None
    return render_template("parking.html", data=data, time_input=time_input)