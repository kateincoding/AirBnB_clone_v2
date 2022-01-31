#!/usr/bin/python3
"""module flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Close SLQAlchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_states_list():
    """html that shows the list of states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
