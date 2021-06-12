import os

import flask
import mwoauth
import yaml
from flask import request, Response

app = flask.Flask(__name__)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', threaded=True, debug=True)

# Load configuration from YAML file
__dir__ = os.path.dirname(__file__)
app.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))


app.route("/")
def index():
   print('index has been called')
   return flask.redirect("/")

app.route("/editing_buddy/")
def buddy():
   print('buddy has been called')
   return flask.redirect("/editing_buddy/")

# @app.route('/')
# def index():
#    greeting = app.config['GREETING']
#    username = flask.session.get('username', None)
#    return flask.render_template(
#        'index.html', username=username, greeting=greeting)


@app.route('/login/')
def login():
    """Initiate an OAuth login.
    
    Call the MediaWiki server to get request secrets and then redirect the
    user to the MediaWiki server to sign the request.
    """
    consumer_token = mwoauth.ConsumerToken(
        app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
    try:
        redirect, request_token = mwoauth.initiate(
            app.config['OAUTH_MWURI'], consumer_token)
    except Exception:
        app.logger.exception('mwoauth.initiate failed')
        return flask.redirect(flask.url_for('index'))
    else:
        flask.session['request_token'] = dict(zip(
            request_token._fields, request_token))
        return flask.redirect(redirect)


@app.route('/oauth-callback/')
def oauth_callback():
    """OAuth handshake callback."""
    if 'request_token' not in flask.session:
        flask.flash(u'OAuth callback failed. Are cookies disabled?')
        return flask.redirect(flask.url_for('index'))

    consumer_token = mwoauth.ConsumerToken(
        app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])

    try:
        access_token = mwoauth.complete(
            app.config['OAUTH_MWURI'],
            consumer_token,
            mwoauth.RequestToken(**flask.session['request_token']),
            flask.request.query_string)

        identity = mwoauth.identify(
            app.config['OAUTH_MWURI'], consumer_token, access_token)
    except Exception:
        app.logger.exception('OAuth authentication failed')

    else:
        flask.session['access_token'] = dict(zip(
            access_token._fields, access_token))
        flask.session['username'] = identity['username']

    return flask.redirect(flask.url_for('index'))


@app.route('/logout/')
def logout():
    """Log the user out by clearing their session."""
    flask.session.clear()
    return flask.redirect(flask.url_for('index'))


@app.route('/git-pull/', methods=['POST'])
def respond():
    print(request.json);
    os.system('git pull')
    return Response(status=200)


@app.errorhandler(404)
def handling_page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# APPS
from view.home import *
from view.editing_buddy_app import *
from view.layouts import *
