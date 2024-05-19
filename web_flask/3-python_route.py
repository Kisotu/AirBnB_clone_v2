#!/usr/bin/python3
"""Task 3 - python is cool"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """return hello hbhb"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """return string provided by user"""

    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """displays “Python ”, followed by the value of the text"""

    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
