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