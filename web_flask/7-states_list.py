#!/usr/bin/python3
"""Starts a Flash Web Application"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of states"""
    states = storage.all('State').values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db_session(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
