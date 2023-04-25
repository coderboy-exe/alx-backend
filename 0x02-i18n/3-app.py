#!/usr/bin/env python3
""" Module definition """

from flask import Flask, render_template, request
from flask_babel import Babel, _
from pytz import UTC


class Config(object):
    """ Config class foe flask_babel instance """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ gets locale best match nased off config """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ index route """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
