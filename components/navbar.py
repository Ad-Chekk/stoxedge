# components/navbar.py
from dash import html, dcc

def create_navbar():
    button_style = {
        'color': 'white',
        'margin': '0 10px',
        'font-size': '16px',
        'background-color': '#555',
        'border': 'none',
        'padding': '10px 20px',
        'text-align': 'center',
        'text-decoration': 'none',
        'display': 'inline-block',
        'cursor': 'pointer',
        'border-radius': '5px'
    }

    return html.Div(
        children=[
            html.Button("Home", id='btn-home', n_clicks=0, style=button_style),
            html.Button("Page 1", id='btn-page-1', n_clicks=0, style=button_style),
            html.Button("Page 2", id='btn-page-2', n_clicks=0, style=button_style),
        ],
        style={
            'background-color': '#333',
            'padding': '10px',
            'color': 'white',
            'text-align': 'center',
            'margin-bottom': '20px'
        }
    )
