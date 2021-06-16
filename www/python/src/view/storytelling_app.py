import sys

sys.path.insert(0, '/www/python/src')

from model.storytelling_model import get_content

# SERVER
from app import app as application
# Dash
from dash import Dash, no_update
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html
# Pandas
import pandas as pd
##Assets
from view.layouts import *

storytelling_app = Dash(__name__, server=application, url_base_pathname="/storytelling/",
                 external_stylesheets=external_stylesheets)
storytelling_app.config['suppress_callback_exceptions'] = True
title = 'Storytelling '
storytelling_app.title = title + title_addenda

storytelling_app.layout = html.Div([
    navbar,
    html.H3(title, style={'textAlign': 'center'}),
    html.Br(),
    #dcc.Markdown(children=get_content('ca','Usuari_Discussió:Bestiasonica')),
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(get_content('ca','Usuari_Discussió:Bestiasonica')),
    #html.Div(children=get_content('ca','Usuari_Discussió:Bestiasonica')),
    html.Br(),
    footbar
])