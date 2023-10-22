#!/usr/bin/python3
"""Run a Flask application with debugging enabled, listening on
'0.0.0.0' and port 5000."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route: /
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
    Displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route: /c/<text>
    Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with spaces.
    """
    return "C " + text.replace("_", " ")


@app.route("/python", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Route: /python or /python/<text>
    Displays 'Python' followed by the value of <text>
    Replaces any underscores in <text> with spaces.
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route: /number/<n>
    Displays '<n> is a number' only if <n> is an integer.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route: /number_template/<n>
    Displays an HTML page only if <n> is an integer.
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
