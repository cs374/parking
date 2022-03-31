from flask import Flask, render_template, request, flash
import psycopg, app

def index():
    term = request.args.get("term", "")

    monday = request.args.get("M", "")
    tuesday = request.args.get("TU", "")
    wednesday = request.args.get("W", "")
    thursday = request.args.get("TH", "")
    friday = request.args.get("F", "")

    #turns separate variables into one string for sql
    day = getDays(monday, tuesday, wednesday, thursday, friday)

    if term and day:
        con = app.return_database()
        cur = con.cursor()
        sql = """
            SELECT to_char(beg_time, 'HH24:MI'), num_students, num_courses
            FROM how_many_stucour(%s, %s);"""
        cur.execute(sql, (term, day))
        try:
            cur.execute(sql, (term, day))

            #if the results are empty
            row = cur.fetchone()
            if row == None:
                flash(f'No significant matches.')
                cur = None

            #turns numerical term into readable term
            strTerm = processStrings(term)
        except Exception as error:
            flash(f'Error in selections.')
            cur = None

        return render_template("how_many_stucour.html", term=term, strTerm=strTerm, day=day, cur=cur)
    else:
        return render_template("how_many_stucour.html")
    
def getDays(mon, tues, wed, thur, fri):
    day = ''
    if mon:
        day += 'M'
    if tues:
        day += 'TU'
    if wed:
        day += 'W'
    if thur:
        day += 'TH'
    if fri:
        day += 'F'

    #handle TT case
    if len(day) > 2:
       day = day.replace('TU', 'T')
       day = day.replace('TH', 'T')


    #handle M-F case
    if mon and tues and wed and thur and fri:
        day = 'M-F'

    return day

def processStrings(term):
    strTerm = ''
    #strDay = ''
    if term == '1211':
        strTerm = 'Spring 2021'
    else:
        strTerm = 'Fall 2021'

    return strTerm
