#!/usr/bin/python3
"""Run a Flask application with debugging enabled, listening on
'0.0.0.0' and port 5000."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """
    Teardown function to close the current session of SQLAlchemy.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Route: /states_list
    Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
