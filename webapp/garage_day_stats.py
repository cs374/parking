from flask import Flask, render_template, request, flash
import psycopg, app

def garage_day_stats():
    """
    cur1 = cursor for generating all the radio buttons dynamically
    cur2 = cursor for generating main query data
    cur3 = cursor for generating the garage name for chart title.
    """
    #make two cursors
    garage = request.args.get("garage", "")
    date = request.args.get("date", "2021-02-17")
    con = app.return_database()
    cur1 = con.cursor()
 
    #used for the form
    cur1.execute("SELECT * FROM garage")
    
    if garage and date:
        cur2 = con.cursor()
        cur3 = con.cursor()
        sql = """
        SELECT to_char(time_stamp, 'HH24:MI'), occ_spaces
        FROM garage_daily_stats(%s, %s)
        ORDER BY time_stamp;"""
        try:
            cur2.execute(sql, (garage, date))
            cur3.execute('SELECT deck, zone FROM garage WHERE zone_id = %s', (garage,) )
            names = cur3.fetchone()
            strGarage = names[0] + ': ' + names[1]
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
        strGarage = None
    
    return render_template("garage_day_stats.html", garage=garage, strGarage = strGarage, date=date, cur1=cur1, cur2=cur2) #pass both cursors to the template

