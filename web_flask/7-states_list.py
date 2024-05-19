#!/usr/bin/python3
"""Task 8 - List of cities"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of state ids"""

    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown context"""

    if storage is not None:
        storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
