#!/usr/bin/python3
"""Run a Flask application with debugging enabled, listening on
'0.0.0.0' and port 5000."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """
    Teardown function to close the current database session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    Route: /cities_by_states
    Displays an HTML page with a list of all State objects.
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
