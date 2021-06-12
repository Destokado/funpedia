import sys

sys.path.insert(0, '/www/python/src')

from model.buddy_model import get_editing_buddy

# SERVER
from app import app as application
# Dash
from dash import Dash, no_update
from dash.dependencies import Input, Output, State
# Pandas
import pandas as pd
##Assets
from view.layouts import *

buddy_app = Dash(__name__, server=application, url_base_pathname="/editing_buddy/",
                 external_stylesheets=external_stylesheets)
buddy_app.config['suppress_callback_exceptions'] = True
title = 'Editing Buddy '
buddy_app.title = title + title_addenda

buddy_app.layout = html.Div([
    navbar,
    html.H3(title, style={'textAlign': 'center'}),
    dcc.Markdown(
        "This page allows you to find the Editing Buddy of a Wikipedia user by entering the username and the Wikipedia Language edition and the namespaces where to look for edits.  "
        "It looks for the contributors of the pages edited by the user in their last 100 edits in the selected namespaces,"),
    dcc.Markdown("* **What is your editing Buddy?**"),
    html.Div(
        html.P('Insert a username'),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Br(),
    html.Div(
        dcc.Input(
            id='username',
            type='text',
            debounce=True,
            # required=True,
            placeholder='Enter your username here',
            style={'width': '190px'}
        ),
    ),
    html.Br(),
    html.Div(
        html.P(
            'Insert the language code of the Wikipedia the user belongs to ( en for English, es for Spanish, ca for Catalan, etc.)'),
        style={'display': 'inline-block', 'width': '600px'}),
    html.Br(),
    html.Div(
        dcc.Input(
            id='languagecode',
            type='text',
            placeholder='Enter the language code here',
            debounce=True,
            # required=True,
            style={'width': '190px'}
        ),
    ),
    html.Br(),
    namespace_picker_multi,
    html.Div(
        html.A(html.Button('Query Results!'),
               id='button'),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Table(id='table'),
    html.P(id='err', style={'color': 'red'}),
    html.Br(),
    footbar

], className="container")


##########CALLBACKS###############
@buddy_app.callback(
    Output('table', 'children'),
    Output('err', 'children'),
    [Input('button', 'n_clicks')],
    state=[State('username', 'value'), State('languagecode', 'value'), State('namespaces', 'value')],
    prevent_initial_call=True)
def build_table(n_clicks, username, languagecode, namespaces):
    print(n_clicks, username, languagecode, namespaces)

    if username is None or languagecode is None or namespaces is None:
        return no_update, 'Fill all the fields before querying'
    # try:
    data = get_editing_buddy(username, languagecode.lower(), namespaces)
    # except Exception:
    #    return no_update, 'No data for User: {} in {}.wikipedia.org in namespaces {}'.format(username, languagecode,
    # namespaces)
    if (len(data) == 0):
        return no_update, 'No data for User: {} in {}.wikipedia.org in namespace/s {}'.format(username, languagecode,
                                                                                             namespaces)

    dataframe = pd.DataFrame(data, columns=['User', 'Coincidences']).sort_values('Coincidences', ascending=False).head(
        10)
    print(dataframe)

    return generate_table(dataframe), ""


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
