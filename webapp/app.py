from typing import ItemsView
from flask import Flask, render_template
from flask_navigation import Navigation

import psycopg
import visitors_per_hour
import class_time_garage_avail
import garage_day_stats
import how_many_stucour
import percentage_occupied
import faculty

app = Flask(__name__)
nav = Navigation(app)
app.secret_key = "key"

# Create Nav Bar
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Visitors', 'visitors'),
    nav.Item('Classes and Parking', 'classtime'),
    nav.Item('Garage per Day', 'garages'),
    nav.Item('Classes and Parking', 'students'),
    nav.Item('Percent Occupied', 'occupied'),
    nav.Item('Faculty Spots', 'facultySpots')
    ])

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=parking password=JUvWSJ2hgRp93TmU")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/visitors")
def visitors():
    return visitors_per_hour.select_garage()

@app.route("/classtime")
def classtime():
    return class_time_garage_avail.select_class_time()

@app.route("/garages")
def garages():
    return garage_day_stats.garage_day_stats()

@app.route("/students")
def students():
    return how_many_stucour.index()

@app.route("/occupied")
def occupied():
    return percentage_occupied.select_hour_date()

@app.route("/faculty")
def facultySpots():
    return faculty.availableSpots()