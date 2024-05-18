#!/usr/bin/python3
"""Task 1 - 2 routes flask app that returns 2 different strings"""

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


if __name__ == "__main__":
    app.run()
