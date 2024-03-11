# pages/home.py
from dash import html, dcc
from components.navbar import create_navbar

layout = html.Div(
    children=[

        html.H1("Home Page"),
        html.P("Welcome to the home page!"),

    ]
)
