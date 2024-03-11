import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

# Layout for the home page
home_layout = html.Div(
    children=[
        html.H1("Home Page"),
        dcc.Link("Go to Page 1", href="/page-1"),
        html.Br(),
        dcc.Link("Go to Page 2", href="/page-2"),
    ]
)

# Layout for Page 1
page_1_layout = html.Div(
    children=[
        html.H1("Page 1"),
        html.P("This is the content of Page 1."),
        dcc.Link("Go back to Home", href="/"),
    ]
)

# Layout for Page 2
page_2_layout = html.Div(
    children=[
        html.H1("Page 2"),
        html.P("This is the content of Page 2."),
        dcc.Link("Go back to Home", href="/"),
    ]
)

# Define the app layout with a dcc.Location component
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return home_layout

if __name__ == '__main__':
    app.run_server(debug=True)

