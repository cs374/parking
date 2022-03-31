from flask import Flask, render_template
import avg_visitors_per_hour
import class_time_garage_avail
import garage_day_stats
import how_many_stucour
import percentage_occupied
import faculty

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/visitors")
def visitors():
    return avg_visitors_per_hour.select_garage()

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