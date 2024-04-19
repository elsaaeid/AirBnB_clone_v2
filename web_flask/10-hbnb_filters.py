#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_page():
    """displays webpage
    Returns:
        HTML Page
    """
    dict_states = storage.all(State)
    dict_amenities = storage.all(Amenity)
    states = []
    amenities = []

    for k, v in dict_states.items():
        states.append(v)
    for k, v in dict_amenities.items():
        amenities.append(v)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
