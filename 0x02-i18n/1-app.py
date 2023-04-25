#!/usr/bin/env python3
""" Module definition """

from flask import Flask, render_template
from flask_babel import Babel
from pytz import UTC


app = Flask(__name__)
babel = Babel(app)

class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = UTC

@app.route('/')
def index():
    """ index route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
