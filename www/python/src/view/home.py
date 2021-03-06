import sys

sys.path.insert(0, '/www/python/src')

# SERVER
from app import app as app
# Dash
from dash import Dash
##Assets
from view.layouts import *


### DASH APP
home_app = Dash(__name__, server=app, url_base_pathname="/", external_stylesheets=external_stylesheets)
home_app.config['suppress_callback_exceptions'] = True

### APP_LAYOUT
home_app.title = 'Home' + title_addenda
home_app.layout = html.Div([
    navbar,

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H2(html.B(' FUNPEDIA'), style={'textAlign': 'center', 'font-weight': 'bold','color':'#FFBD59'}),
    html.Div(
        dcc.Markdown('''
    Providing gamified activities to enhance community health and content creation in a fun way.'''.replace('  ', '')),
        style={'textAlign': 'center'}, ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    footbar,

], className="container")

