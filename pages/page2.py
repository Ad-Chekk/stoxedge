# pages/page2.py
from dash import html
from components.navbar import create_navbar
layout = html.Div(
    children=[

        html.H1("Page 2"),
        html.P("This is the content of Page 2."),
    ]
)
