#!/usr/bin/python3
"""Run a Flask application with debugging enabled, listening on
'0.0.0.0' and port 5000."""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Route: /hbnb_filters
    Displays the HBnB filters HTML page.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return (render_template("10-hbnb_filters.html",
                            states=states, amenities=amenities))


@app.teardown_appcontext
def teardown(excpt=None):
    """
    Teardown function to remove the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
