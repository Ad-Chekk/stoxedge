# pages/page1.py
from dash import html, dcc
from components.navbar import create_navbar

layout = html.Div(
    children=[

        html.H1("Page 1"),
        html.P("This is the content of Page 1."),

        html.Label("Age:"),
        dcc.Input(id='input-age', type='number', value=25),
        html.Br(),

        # Gender input box
        html.Label("Gender:"),
        dcc.Input(id='input-gender', type='text', placeholder='Enter gender'),
        html.Br(),

        # Location input box
        html.Label("Location:"),
        dcc.Input(id='input-location', type='text', placeholder='Enter location'),
        html.Br(),

        # Type of residence input box
        html.Label("Type of Residence:"),
        dcc.Input(id='input-residence', type='text', placeholder='Enter residence type'),
        html.Br(),

        html.Button(children='Submit', id='input-submit', n_clicks=0),

        html.Div(id='output-div', children=[]),
    ]
)
