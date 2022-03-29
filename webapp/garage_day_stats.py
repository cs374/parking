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
        return render_template("garage_day_stats.html", cur=cur)
    else:
        return render_template("garage_day_stats.html")
