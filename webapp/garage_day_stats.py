from flask import Flask, render_template, request, flash
import psycopg, app

def garage_day_stats():
    #make two cursors
    garage = request.args.get("garage", "")
    date = request.args.get("date", "")
    con = app.return_database()
    cur1 = con.cursor()
 
    #used for the form
    cur1.execute("SELECT * FROM garage")
    
    if garage and date:
        cur2 = con.cursor()
        sql = """
        SELECT time_stamp::time, occ_spaces
        FROM garage_daily_stats(%s, %s)
        ORDER BY time_stamp;"""
        try:
            cur2.execute(sql, (garage, date))
        except Exception as error:
            flash(f'Error in selections.')
            cur2 = None
            
        #if the results are empty
        row = cur2.fetchone()
        if row == None:
            flash(f'No valid matches.')
            cur2 = None
    else:
        cur2 = None
    
    return render_template("garage_day_stats.html", garage=garage, date=date, cur1=cur1, cur2=cur2) #pass both cursors to the template

