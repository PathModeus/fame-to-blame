import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import subprocess

def appli(datafram) : 
    markdown_text = '''
    ### Pull up
    Gif Bézos sacrée bande de toquards
    ''' 


    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    df =  pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


    def generate_table(dataframe, max_rows=10):
         return html.Table(
    # Header
    [html.Tr([html.Th(col) for col in dataframe.columns])] +
    # Body
    [html.Tr([
    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
    ]) for i in range(min(len(dataframe), max_rows))]
    )


    app.layout = html.Div(children=[
        html.H1(children='Fame-to-Blame'),
        dcc.Markdown(children=markdown_text),
        html.Label('Languages'),
        dcc.Dropdown(
        options=[
        {'label': 'French', 'value': 'FR'},
        {'label': u'English', 'value': 'EN'},
        ],
        value='EN'
        ),
        html.Label('Nombre de tweets chargés'),
        dcc.Slider(
        min=10,
        max=1000,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in [10,100,200,500,1000]},
        value=10,
        ),
        dcc.Graph(
            id='example-graph',
            figure={
            'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
            'title': 'Dash Data Visualization'
            }
            }
        ),
        html.H4(children='Classement des célébrités les plus frequemment insultées sur Twitter'),
        generate_table(datafram)])
        
    app.run_server(debug=True)
    
