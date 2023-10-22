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
    @app.route('/states', strict_slashes=False)
    @app.route('/states/<state_id>', strict_slashes=False)
    def cities_by_states(state_id=None):
    
    states = storage.all(State)
    state = None

    if state_id:
        state = states.get(state_id)

    return render_template('9-states.html', states=states.values(),
                           state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
