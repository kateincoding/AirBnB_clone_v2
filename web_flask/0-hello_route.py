#!/usr/bin/python3
"""module hello route of flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """print first message"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
