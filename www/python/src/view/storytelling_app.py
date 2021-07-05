import sys

sys.path.insert(0, '/www/python/src')

# SERVER
from app import app as application
# Dash
from dash import Dash
# Pandas
##Assets
from view.layouts import *

storytelling_app = Dash(__name__, server=application, url_base_pathname="/storytelling/",
                        external_stylesheets=external_stylesheets)
storytelling_app.config['suppress_callback_exceptions'] = True
title = 'Storytelling '
storytelling_app.title = title + title_addenda

storytelling_app.layout = html.Div([
    navbar,
    html.Br(),
    html.H3(title, style={'textAlign': 'center'}),
    html.Br(),
    dcc.Markdown(
        """This activity consists of telling invented (or not) stories based on a selection of random articles, within the articles that the user has edited or created.  
        These articles serve to inspire and guide the story, and not all of them need to be used. Each story is considered a thread, other users can continue the story, again requesting random articles and using them as much as possible to follow the thread, indefinitely or until the original author closes the story.   
        Users can **vote** on other users' contributions and **report** them if they are offensive, disruptive (troll) or lack syntax and spelling."""),
    html.Br(),
    footbar
], className="container")
