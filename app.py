# app.py
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pages import home, page1, page2
from components import navbar

app = dash.Dash(__name__, suppress_callback_exceptions=True)

#User input will be strored here
user_inputs = []


# Define the app layout with a dcc.Location component
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar.create_navbar(),
    html.Div(id='page-content')
])

# Callback to update the page content and button styles based on clicks
@app.callback(
    [Output('page-content', 'children'),
     Output('btn-home', 'style'),
     Output('btn-page-1', 'style'),
     Output('btn-page-2', 'style')],
    [Input('btn-home', 'n_clicks'),
     Input('btn-page-1', 'n_clicks'),
     Input('btn-page-2', 'n_clicks')],
    [State('url', 'pathname')]
)
def display_page_and_color_change(btn_home, btn_page_1, btn_page_2, current_path):
    ctx = dash.callback_context
    button_id = ctx.triggered_id.split('.')[0] if ctx.triggered_id else None

    # Default styles for buttons
    default_style = {'font-size': '16px', 'background-color': '#555', 'color': 'white'}

    # Highlight color for clicked button
    highlight_style = {'background-color': 'pink'}

    # Apply default style to all buttons
    style_home = style_page_1 = style_page_2 = default_style

    # Apply highlight style to the clicked button
    if button_id == 'btn-home':
        style_home = {**default_style, **highlight_style}
        page_content = home.layout
    elif button_id == 'btn-page-1':
        style_page_1 = {**default_style, **highlight_style}
        page_content = page1.layout
    elif button_id == 'btn-page-2':
        style_page_2 = {**default_style, **highlight_style}
        page_content = page2.layout
    elif current_path:
        # If no button is clicked, default to the current URL path
        page_content = home.layout

    return page_content, style_home, style_page_1, style_page_2

# Callback to save user inputs
@app.callback(Output('output-div', 'children'),
              [Input('input-submit', 'n_clicks')],
              [State('input-age', 'value'),
               State('input-gender', 'value'),
               State('input-location', 'value'),
               State('input-residence', 'value')])
def save_user_inputs(n_clicks, age, gender, location, residence):
    if n_clicks:
        user_inputs.append({
            'age': age,
            'gender': gender,
            'location': location,
            'residence': residence
        })

        data_to_display = [html.P(f"{key}: {value}") for entry in user_inputs for key, value in entry.items()]

        return f'Data saved: {user_inputs}, {data_to_display}'









if __name__ == '__main__':
    app.run_server(debug=True)
