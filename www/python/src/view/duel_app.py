import sys
from datetime import datetime

import dash_table
from dash.dependencies import Input, State, Output

from www.python.src.model.duel_model import insert_into, select_duels

sys.path.insert(0, '/www/python/src')

# SERVER
from app import app as application
# Dash
from dash import Dash
# Pandas
import pandas as pd
##Assets
from view.layouts import *
from model.duel_model import *

metrics_dict = {'Edit Count': 'edit_count'}

duel_app = Dash(__name__, server=application, url_base_pathname="/duel/",
                external_stylesheets=external_stylesheets)
duel_app.config['suppress_callback_exceptions'] = True
title = 'Duel '
duel_app.title = title + title_addenda

duel_app.layout = html.Div([
    navbar,
    html.H3(title, style={'textAlign': 'center'}),
    dcc.Markdown("""This page allows you to challenge another editor to contribute.  
    You can establish a metric (rule to measure the duel), an objective, the language edition, the duration and the namespaces in which the duel will take place. **You can also agree on themes (Wikipedia categories) and even bet points!**   
    Remember: whoever reaches the goal first or whoever is closest to it when the final date arrives, wins the duel and gets the tokens from the bet, if any."""),
    dcc.Markdown("* **Do you have what it takes?**"),
    html.Div(
        html.P('Insert your username'),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Br(),
    html.Div(
        dbc.Input(
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
            'Insert the language code of the Wikipedia the user belongs to (en for English, es for Spanish, ca for Catalan, etc.)'),
        style={'display': 'inline-block', 'width': '600px'}),
    html.Div(
        dcc.Input(
            id='languagecode',
            type='text',
            placeholder='Enter the language code here',
            debounce=True,

            style={'width': '190px'}
        ),
    ),
    html.Br(),
    html.Div(
        html.P('Rival username'),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Br(),
    html.Div(
        dbc.Input(
            id='rival_username',
            type='text',
            debounce=True,
            # required=True,
            placeholder='Enter your rival username here',
            style={'width': '190px'}
        ),
    ),
    html.Br(),
    html.Div(
        html.P(
            'Insert the language code of the Wikipedia your rival belongs to.'),
        style={'display': 'inline-block', 'width': '600px'}),

    html.Br(),
    html.Div(
        dcc.Input(
            id='rival_languagecode',
            type='text',
            placeholder='Enter the language code here',
            debounce=True,
            # required=True,
            style={'width': '190px'}
        ),
    ),
    html.Br(),
    namespace_picker_multi,
    html.Br(),
    html.Div([
        html.Div(
            html.P('Select the metric '),
            style={'display': 'inline-block', 'width': '200px'}),
        html.Br(),
        html.Div(
            dcc.Dropdown(
                id='metric',
                options=[{'label': k, 'value': v} for k, v in metrics_dict.items()],
                value=0,
                multi=True,
                style={'width': '190px'}
            ), style={'display': 'inline-block', 'width': '200px'}),

    ]),
    html.Br(),
    html.Div([
        html.P(
            'Insert the goal'),
        dcc.Input(
            id='goal',
            type='text',
            placeholder='Enter the goal',
            debounce=True,
            style={'width': '190px'}
        ), html.Br()
    ],
        style={'display': 'inline-block', 'width': '600px'}),
    html.Br(),
    html.Div([
        dcc.Input(id="start", placeholder='Start date (DD/MM/YYYY)'),
        dcc.Input(id="end", placeholder="End date (DD/MM/YYYY)")]
    ),
    html.Div(
        html.A(html.Button('START DUEL'),
               id='button_start', style={'color': '#FFBD59'}),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Div(dbc.Spinner(children=[html.Table(id='table')], type='default')),
    dbc.Alert(id='err', color="warning", dismissable=True, is_open=False),
    html.Br(),
    html.Div(
        html.A(html.Button('VIEW DUELS'),
               id='button_view', style={'color': '#FFBD59'}),
        style={'display': 'inline-block', 'width': '200px'}),
    html.Div(dbc.Spinner(children=[html.Table(id='duel_table')], type='default')),
    html.Br(),
    html.H2('Current duels'),
    html.Table(id='current_duels'),
    footbar, ], className="container")


########CALLBACKS############
@duel_app.callback(Output('err', 'children'),
                   Output('err', 'is_open'), [Input('button_start', 'n_clicks')],
                   state=[State('username', 'value'), State('languagecode', 'value'), State('rival_username', 'value'),
                          State('rival_languagecode', 'value'), State('metric', 'value'), State('goal', 'value'),
                          State('namespaces', 'value'), State('start', 'value'), State('end', 'value')],
                   prevent_initial_call=True)
def regiter_duel(n_clicks, username, languagecode, rival_username, rival_languagecode, metric, goal, namespaces, start,
                 end):
    print("called")
    if username is None or languagecode is None or namespaces is None or rival_username is None or rival_languagecode \
            is None or metric is None or goal is None or start is None or end is None:
        return 'Fill all the required fields before querying (all excpet namespaces)', True

    columns = ["user_name", "user_wiki", "rival_name", "rival_wiki", "metric", "goal", "start_date",
               "end_date"]
    date_start = datetime.strptime(start, "%d/%m/%Y").timestamp()
    date_end = datetime.strptime(end, "%d/%m/%Y").timestamp()
    row = [username, languagecode, rival_username, rival_languagecode, metric[0], goal, date_start,
           date_end]
    if (namespaces is not None):
        columns.append("namespaces")
        if (not isinstance(namespaces, int)):
            row.append(",".join(namespaces))
        else:
            row.append(str(namespaces))
    try:
        inserted = insert_into("duels", columns, tuple(row))
        print(inserted)
    except Exception:
        return "Something went wrong", True

    return "Inserted {} row in the database.".format(inserted), True


@duel_app.callback(Output('current_duels', 'children'), Input('button_start', 'n_clicks'))
def fetch_duel(n_clicks):
    data = select_duels(['user_name', 'user_wiki', 'rival_name', 'rival_wiki', 'metric', 'goal', 'start_date',
                         'end_date', 'namespaces'])
    df = pd.DataFrame(data, columns=['Username', 'Wikipedia', 'Rival', 'Rival Wikipedia', 'Metric', 'Goal',
                                     'Start date', 'End date', 'Namespaces'])
    print(df.head())
    df['Start date'] = df['Start date'].apply(lambda x: datetime.utcfromtimestamp(x).date().strftime("%d/%m/%Y"))
    df['End date'] = df['End date'].apply(lambda x: datetime.utcfromtimestamp(x).date().strftime("%d/%m/%Y"))
    return dash_table.DataTable(columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict('records'), )
