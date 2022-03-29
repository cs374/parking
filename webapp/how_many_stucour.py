from flask import Flask, render_template, request
import psycopg

app = Flask(__name__)


@app.route("/")
def index():
    term = request.args.get("term", "")
    day = request.args.get("day", "")
    if term and day:
        con = psycopg.connect(
            "host=localhost dbname=parking user=hendrijn password=112259998")
        cur = con.cursor()
        sql = """
            SELECT *
            FROM how_many_stucour(%s, %s);"""
        cur.execute(sql, (term, day))
        strTerm, strDay = processStrings(term, day)
        return render_template("how_many_stucour.html", term=strTerm, day=strDay, cur=cur)
    else:
        return render_template("how_many_stucour.html")
    

def processStrings(term, day):
    strTerm = ''
    strDay = ''
    if term is '1211':
        strTerm = 'Spring 2021'
    else:
        strTerm = 'Fall 2021'

    if 'M' in day:
        strDay += 'Monday'
    if 'TU' in day:
        strDay += 'Tuesday'
    if 'W' in day:
        strDay += 'Wednesday'
    if 'TH' in day:
        strDay += 'Thursday'
    if 'F' in day:
        strDay += 'Friday'
    if 'TT' in day:
        strDay += 'Tuesday and Thursday'

    return strTerm, strDay
