import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import sys

sys.path.insert(0, '/www/python/src')

external_stylesheets = [dbc.themes.BOOTSTRAP]
navbar = dbc.Navbar(
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

                ], className="ml-auto", navbar=True),
            id="navbar-collapse2",
            navbar=True,
        ),
        ],
        color="#FFEACA",
        dark=False,
        className="ml-2",
        sticky='top'
    )
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

language_picker_multi = html.Div([])

namespaces_dict = {
    "Article (0)": 0, "Talk (0)": 1,
    "User (2)": 2, "User talk (3)": 3,
    "Wikipedia (4)": 4, "Wikipedia talk (5)": 5,
    "File (6)": 6, "File talk (7)": 7,
    "MediaWiki (8)": 8, "MediaWiki talk (9)": 9,
    "Template(10)": 10, "Template talk (11)": 11,
    "Help (12)": 12, "Help talk (12)": 12,
    "Category (14)": 14, "Category talk (14)": 15,
    "Portal (11)": 100, "Portal talk (101)": 101,
    "Draft (118)": 118, "Draft talk (119)": 119,
    "TimedText (710)": 710, "TimedText talk (711)": 711,
    "Module (828)": 828, "Module talk (829)": 829}

namespace_picker_multi = html.Div([
        html.Div(
            html.P('Select the namespaces '),
            style={'display': 'inline-block', 'width': '200px'}),
        html.Br(),
        html.Div(
            dcc.Dropdown(
                id='namespaces',
                options=[{'label': k, 'value': v} for k,v in namespaces_dict.items()],
                value=0,
                multi=True,
                style={'width': '190px'}
            ), style={'display': 'inline-block', 'width': '200px'}),

])

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