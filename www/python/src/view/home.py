import sys

sys.path.insert(0, '/www/python/src')

# SERVER
from app import app as application

# Dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

##Assets
external_stylesheets = [dbc.themes.BOOTSTRAP]
navbar = html.Div([
    html.Br(),
    dbc.Navbar(
        [dbc.Collapse(
            dbc.Nav(
                [
                    dbc.DropdownMenu(
                        [dbc.DropdownMenuItem("Find your Editing Buddy",
                                              href="https://funpedia.toolforge.org/editing_buddy/"),
                         dbc.DropdownMenuItem("Storytelling", href="https://funpedia.toolforge.org/storytelling/"),
                         ],
                        label="Social Gamification",
                        nav=True,
                    ),
                    dbc.DropdownMenu(
                        [dbc.DropdownMenuItem("Duel", href="https://funpedia.toolforge.org/duel/")
                         ],
                        label="Content Gamification",
                        nav=True,
                    ),
                    html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src= 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png', height="35px")),
                                #
                            ],
                            align="center",
                            no_gutters=True,
                        ),
                        href="https://github.com/Destokado/funpedia", target="_blank",
                        style={'margin-left': "5px"}),
                ], className="ml-auto", navbar=True),
            id="navbar-collapse2",
            navbar=True,
        ),
        ],
        color="white",
        dark=False,
        className="ml-2",
    ),
])
footbar = html.Div([
    html.Br(),
    html.Br(),
    html.Hr(),

    html.Div(
        dbc.Nav(
            [
                dbc.NavLink("Gamification", href="https://en.wikipedia.org/wiki/Gamification", target="_blank",
                            style={'color': '#8C8C8C'}),
                dbc.NavLink("View Source", href="https://github.com/Destokado/funpedia", target="_blank",style={'color': '#8C8C8C'}),
                dbc.NavLink("Author", href="https://meta.wikimedia.org/wiki/User:Destokado", target="_blank",style={'color': '#8C8C8C'}),

            ], className="ml-2"), style={'textAlign': 'center', 'display': 'inline-block', 'width': '60%'}),

    html.Br(),
    html.Div([
        html.P('Hosted with ♥ on ', style={'display': 'inline-block'}),
        html.A('Toolforge', href='https://wikitech.wikimedia.org/wiki/Portal:Cloud_VPS', target="_blank",
               style={'display': 'inline-block'}),
        html.P('.', style={'display': 'inline-block', 'margin-right': "5px"}),
        html.A(html.Img(src='https://upload.wikimedia.org/wikipedia/commons/c/c5/Toolforge_logo.svg',
                        height="35px"), href='https://wikitech.wikimedia.org/wiki/Portal:Toolforge', target="_blank",
               style={'display': 'inline-block'}),
        html.Br(),

        html.P('Added to the ', style={'display': 'inline-block'}),
        html.A(' Open Gamification Code of Ethics', href='https://ethics.gamified.uk?ref=b400', target="_blank",
                style={'display': 'inline-block'}),

        html.P('.', style={'display': 'inline-block', 'margin-right': "5px"}),
        html.A(html.Img(src='https://ethics.gamified.uk/assets/ogce-badge-400.png',

                        height="35px"), href='https://ethics.gamified.uk?ref=b400', target="_blank",

               style={'display': 'inline-block'}),

    ], style={'textAlign': 'right'}
    ),
    html.Br(),


])

title_addenda = " -Funpedia"

### DASH APP
home_app = Dash(__name__, server=application, url_base_pathname="/", external_stylesheets=external_stylesheets)
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
    html.H2(html.B('Welcome to FUNPEDIA'), style={'textAlign': 'center', 'font-weight': 'bold'}),
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
