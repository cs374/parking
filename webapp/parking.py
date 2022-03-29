from flask import Flask, render_template, request, flash, redirect
import psycopg, re

app = Flask(__name__)
app.secret_key = "my_key"

query = """
SELECT * FROM class_time_garage_avail(%s)
"""

def return_database():
    return psycopg.connect("host=localhost dbname=parking user=tranaa password=112099828")

@app.route('/')
def select_class_time():
    #This variable checks if the input is the right format. If it's not the right format,
    #it will be changed to 1. 
    is_input_wrong = None
    time_input = request.args.get("time_input", "")
    if time_input:
        #This regular expression is used for checking the format of the input. 
        #If the input is correct, we can execute the query. 
        if re.match('^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time_input): 
            db = return_database()
            current = db.cursor()
            current.execute(query, (time_input,))
            data=current.fetchall()
        #If the input is the wrong format, render the template without executing the query.
        #Also, now that is_input_wrong is 1, the rendered template will know that it needs
        #to display an error message. 
        else :
            data=None
            is_input_wrong = 1
            return render_template("parking.html", data=data, time_input=time_input, is_input_wrong=is_input_wrong)
    #There's no input, so nothing happens!
    else:
        data = None
    return render_template("parking.html", data=data, time_input=time_input, is_input_wrong=is_input_wrong)