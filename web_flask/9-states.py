#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/')
@app.route('/states/<id>')
def states_and_state(id=None):
    """
    lists of all State objects present in DBStorage sorted by name (A->Z)
    """
    if id not None and id != "":
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


@app.teardown_appcontext
def teardown(exception):
    """
    removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
