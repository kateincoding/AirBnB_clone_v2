#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def deploy_hbnb():
    """deploy a webpage"""
    all_states = storage.all('State').values()
    # """by id"""
    # for state in storage.all("State").values():
        # if state.id == id:
            # return render_template("9-states.html", state=state)
    return render_template("10-hbnb_filters.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
