#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import *
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display an HTML page with the list of all states sorted by name (A->Z)
    """
    states = sorted(list(storage.all("State").values()), key=lambda i: i.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Calls the storage.close() method
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
