# Flask Dt

This is a script to help you display any of the tables in your db using SQLAlchemy in your Flask Routes

## Installation

Run the following to install:

```python
pip install flask-dt
```

## Usage

```python
from flask_dt import FlaskDt

# after declaring your Flask app and SQLAlchemy db instances plus any other additional instances  
# assuming your Flask app and SQLAlchemy db instances are named app and db respectively  

dt = FlaskDt(app, db, "templatename.html", "route")


# This will be called when specifying your routes
dt.display_table()  
```
You will find a simple flask application that utilises flask-dt [here](https://github.com/GreatDt1/Flaskdt_App)
