*** Creating Your Virtual Enviornment ***

Windows OS: 

    1. Navigate into the folder where you want your virtual enviroment (\webapp).
    2. In the terminal type 'py -3 -m venv venv'
    3. Activate the virtual enviornment by typing 'venv\Scripts\activate' in the terminal.

Mac/Linux OS: 

    1. Navigate into the folder where you want your virtual environment (\webapp).
    2. In the terminal type 'python3 -m venv venv'
    3. Activate the virtual enviornment by typing '. venv/bin/activate' in the terminal.

*** Installing all of the Requirements ***

Within the virtual environment in the webapp folder, you will need to install all of the requirements for this app. 
In the terminal, within the virtual environment in the webapp folder, type 'pip install -r requirements.txt' 

*** Nav Bar ***

Each html file has an include statement. To set the active link within the navbar, set the abbreviation to True. Inside the nav.html, jinja statements check which link should have the active class.

The navbar is built with bootstrap 5.1.3. The import links are in the head of nav.html.

*** Static file ***

Please don't rename the static folder!!! That's how flask wants you to store css files and it will give you errors if you change the folder name. 
