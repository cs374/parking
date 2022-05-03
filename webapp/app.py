from flask import Flask, render_template
from visitors_per_hour import select_garage
from garage_day_stats import garage_day_stats
from how_many_stucour import student_courses
from percentage_occupied import select_hour_date
from faculty import availableSpots
import psycopg

app = Flask(__name__)
app.secret_key = "key"

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=parking password=JUvWSJ2hgRp93TmU")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/percent_stu")
def percent_stu():
    return render_template("percent_stu_combo.html")

@app.route("/visitors")
def visitors():
    return select_garage()

@app.route("/garages")
def garages():
    return garage_day_stats()

@app.route("/students")
def students():
    return student_courses()

@app.route("/occupied")
def occupied():
    return select_hour_date()

@app.route("/faculty")
def facultySpots():
    return availableSpots()