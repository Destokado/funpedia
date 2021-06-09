# -*- coding: utf-8 -*-
#
# This file is part of the Toolforge Flask + OAuth WSGI tutorial
#
# Copyright (C) 2017 Bryan Davis and contributors
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
import flask
from flask import request, Response
from dash import Dash
import mwoauth
import os
import yaml

#application = Dash(__name__)
#if __name__ == '__main__':
#    application.run_server(debug=True)

application = flask.Flask(__name__)

if __name__ == '__main__':
    application.run_server(host='0.0.0.0', threaded=True,debug=True)


# Load configuration from YAML file
__dir__ = os.path.dirname(__file__)
application.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))




application.route('/')
def index():

    return flask.redirect('/')

#@app.route('/')
#def index():
#    greeting = app.config['GREETING']
#    username = flask.session.get('username', None)
#    return flask.render_template(
#        'index.html', username=username, greeting=greeting)


@application.route('/login')
def login():
    """Initiate an OAuth login.
    
    Call the MediaWiki server to get request secrets and then redirect the
    user to the MediaWiki server to sign the request.
    """
    consumer_token = mwoauth.ConsumerToken(
        application.config['CONSUMER_KEY'], application.config['CONSUMER_SECRET'])
    try:
        redirect, request_token = mwoauth.initiate(
            application.config['OAUTH_MWURI'], consumer_token)
    except Exception:
        application.logger.exception('mwoauth.initiate failed')
        return flask.redirect(flask.url_for('index'))
    else:
        flask.session['request_token'] = dict(zip(
            request_token._fields, request_token))
        return flask.redirect(redirect)


@application.route('/oauth-callback')
def oauth_callback():
    """OAuth handshake callback."""
    if 'request_token' not in flask.session:
        flask.flash(u'OAuth callback failed. Are cookies disabled?')
        return flask.redirect(flask.url_for('index'))

    consumer_token = mwoauth.ConsumerToken(
        application.config['CONSUMER_KEY'], application.config['CONSUMER_SECRET'])

    try:
        access_token = mwoauth.complete(
            application.config['OAUTH_MWURI'],
            consumer_token,
            mwoauth.RequestToken(**flask.session['request_token']),
            flask.request.query_string)

        identity = mwoauth.identify(
            application.config['OAUTH_MWURI'], consumer_token, access_token)
    except Exception:
        application.logger.exception('OAuth authentication failed')
    
    else:
        flask.session['access_token'] = dict(zip(
            access_token._fields, access_token))
        flask.session['username'] = identity['username']

    return flask.redirect(flask.url_for('index'))


@application.route('/logout')
def logout():
    """Log the user out by clearing their session."""
    flask.session.clear()
    return flask.redirect(flask.url_for('index'))

@application.route('/git-pull', methods=['POST'])
def respond():
    print(request.json);
    os.system('git pull')
    os.system('webservice restart')
    return Response(status=200)

@application.errorhandler(404)
def handling_page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


#APPS
from view.home import *