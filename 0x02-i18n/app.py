#!/usr/bin/env python3
""" Module definition """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from datetime import datetime


class Config(object):
    """ Config class foe flask_babel instance """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Gets user by user_id from user data table """
    keys = users.keys()
    user_id = request.args.get('login_as')

    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """ Set user as global on flask.g.user"""
    g.user = get_user()
    user_tz = get_timezone()

    time = pytz.timezone(user_tz)
    time_format = '%b %d, %Y, %I:%M:%S %p'

    curr_time = datetime.now(time).strftime(time_format)
    g.time = curr_time


@babel.localeselector
def get_locale():
    """ gets locale best match based off config """
    locales = app.config['LANGUAGES']
    locale = request.args.get('locale')

    if g.user is not None and g.user.get('locale') in locales:
        return g.user.get('locale')

    if locale and locale in locales:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """gets timezone best match based off user preference or UTC"""
    tz = request.args.get('timezone')

    if g.user and g.user.get('timezone'):
        tz = g.user.get('timezone')

    if tz:
        try:
            pytz.timezone(tz)
        except UnknownTimeZoneError:
            tz = None
        return tz

    return 'UTC'


@app.route('/', strict_slashes=False)
def index():
    """ index route """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
