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
# assuming your SQLAlchemy db instance is named db

dt = FlaskDt(db)


# This will be called when specifying your routes
@app.route('/tables/<string:tablename>')
@dt.display_table
def your_func():
    pass
```
You will find a simple flask application that utilises flask-dt [here](https://github.com/GreatDt1/Flaskdt_App)

## Maintainer

[<img src="https://avatars.githubusercontent.com/u/68665787?v=4" width = "80" height = "80"/>](https://github.com/Donatussss/)