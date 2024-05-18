#!/usr/bin/python3
"""Task 2 - route that returns  string provided by user"""

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


if __name__ == "__main__":
    app.run()
