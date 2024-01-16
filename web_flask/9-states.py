#!/usr/bin/python3
"""Starts a Flash Web Application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=''):
    """Displays a HTML page with a list of states, and cities from a state"""
    all_states = storage.all(State)
    selected_state = all_states.get(f'State.{id}') if id else None

    template_context = {
            'id': id,
            'all_states': all_states.values(),
            'selected_state': selected_state
            }

    return render_template('9-states.html', **template_context)


@app.teardown_appcontext
def close_db_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
