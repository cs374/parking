from datetime import date
from flask import Flask, render_template, request, flash, redirect
import psycopg, re, app, datetime

def percent_stu_combo():
    hour = request.args.get("hour")
    date = request.args.get("date")

    # HANDLE THE PERCENT OCCUPIED CHART DATA
    garage_space_data = get_garage_spaces()
    percent_data, is_input_wrong = select_hour_date(hour, date)

    if not hour and not date:
        hour='10'
        date="2021-02-17"

    # HANDLE THE STUCOUR CHART DATA
    term = get_term(date)
    dow = get_dayofweek(date)

    stu_data, stu_error = get_student_courses(term, dow)

    #turns numerical term into readable term
    strTerm = processStrings(term)

    return render_template('percent_stu.html', 
        #used for the percent table
        data=garage_space_data, percent_data=percent_data, is_input_wrong=is_input_wrong, hour_input=hour, date_input=date,
        #used for the student table
        stu_data=stu_data, stu_error=stu_error, strTerm=strTerm, day=dow)

def get_garage_spaces():
    # Gets each deck with it's corresponding number of spaces

    query = """
    SELECT deck, sum(spaces) 
    FROM garage
    GROUP BY deck
    ORDER BY deck;
    """
    db = app.return_database()
    current = db.cursor()
    current.execute(query,)
    data=current.fetchall()
    return data

def select_hour_date(hour_input, date_input):
    # Executes the logic for getting the percentage_occupied data

    query = """
    SELECT deck, avg_occupied
	FROM percentage_occupied(%s, %s);
    """

    is_input_wrong = None
    if hour_input and date_input:
        if re.match('^[0-9][0-9]$', hour_input) and int(hour_input) < 24:
            db = app.return_database()
            current = db.cursor()
            current.execute(query, (hour_input, date_input,))
            data=current.fetchall()
        else:
            data=None
            is_input_wrong = 1
            return data, is_input_wrong
    else:
        data=None
        hour_input='10'
        date_input="2021-02-17"

    return data, is_input_wrong


def get_dayofweek(date):
    # Gets the letter for the day of the week
    db = app.return_database()
    current = db.cursor()
    current.execute(f'SELECT EXTRACT(DOW FROM DATE \'{date}\')',)
    result=current.fetchone()
    i = int(result[0])

    days = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']

    return days[i-1] 


def get_term(date):
    # Turns the date into the term
    term = f'1{date[2:4]}'
    month = date[5:7]

    if month[0] == '0':
        month = month[1]

    # Determine starting month of the semester
    if int(month) < 8 and int(month) > 0:
        term += '1'

    return int(term)

def get_student_courses(term, dow):
    # Executes the query for getting student/course info

    con = app.return_database()
    cur = con.cursor()
    sql = """
        SELECT to_char(beg_time, 'HH24:MI'), num_students, num_courses
        FROM how_many_stucour(%s, %s);"""
    cur.execute(sql, (term, dow))
    error = ""
    try:
        cur.execute(sql, (term, dow))

        #if the results are empty
        row = cur.fetchone()
        if row == None:
            error='No significant matches for this date.'
            cur = None
    except Exception as error:
        error = 'Error in selections.'
        cur = None

    return cur, error

def processStrings(term):
    strTerm = ''
    #strDay = ''
    if term == '1211':
        strTerm = 'Spring 2021'
    else:
        strTerm = 'Fall 2021'

    return strTerm