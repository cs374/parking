*** EDIT TO NAV BAR ***
Python 10 has issues loading the Navigation module. Switched to a bootstrap navbar instead. Will delete the below instructions once I confirm how to set the active tab in the bootstrap framework.


*** To View the Navigation Bar ***
- inside of venv, install the Flask-Navigation module as follows...
1. Open up the virtual environment
     # Linux
     source .venv/bin/activate

     # macOS
     source .venv/bin/activate

     # Windows
     .venv\scripts\activate
2. Install the module

    pip install Flask-Navigation
    
3. In the main app.py, import and initialize

    from flask_navigation import Navigation
    
    ...
    
    nav = Navigation(app)
    
