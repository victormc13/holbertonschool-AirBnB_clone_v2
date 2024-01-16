#!/usr/bin/python3
"""Starts a Flash Web Application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_db_session(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """Displays a HTML page with a list of cities by states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
