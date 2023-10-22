#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """removes the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays list of all State objects present in DBStorage sorted alphabetical
    """
    states = storage.all(State)
    states_list = sorted(list(states.values()))
    return render_template('8-cities_by_states.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
