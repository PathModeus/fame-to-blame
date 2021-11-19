import dash
from dash.html.Center import Center
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import webbrowser
from threading import Timer
from flask import request

def appli(datafram) : 
    """Returns a dashboard where our statistics are displayed

    Parameters
    ----------
    A dataframe with a column frequency
    """

    datafram = datafram.sort_values(by=['frequency'], ascending = False)
    """Sort the datafram"""



    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    """loads the datafram"""
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
    ]) for i in range(min(len(dataframe), max_rows))] , 
    style = {'textAlign' : 'center', 'color' :  '#111111'})



    """Generates the dashboard components"""
    colors = {'background' : '#111111', 'text' : '#7FDBFF', 'bodyColor' : '#F2DFCE'}
    def get_page_heading_style() : 
        return {'backgroundcolor' : colors['background']}
    def get_page_heading_title() : 
        return html.H1(children = 'Fame-to-Blame' , style = {'textAlign' : 'center' , 'color' : colors['text']})
    def get_page_heading_subtitle() : 
        return html.Div(children = 'Interactive dashboard providing some statistics to analyse harassment on Twitter', 
                        style = {'textAlign' : 'center', 'color' : colors['text']})
    def generate_page_header() : 
        main_header = dbc.Row([dbc.Col(get_page_heading_title(), md=12)],
                               align = 'center',
                               style = get_page_heading_style()
        )
        subtitle_header = dbc.Row([dbc.Col(get_page_heading_subtitle(), md=12)],
                                    align = 'center',
                                    style = get_page_heading_style()
        )
        header = (main_header, subtitle_header)
        return header
    def generate_layout() : 
        page_header = generate_page_header()
        layout = dbc.Container([
                    page_header[0],
                    page_header[1],
                    html.Hr(),
                    html.Div(children = [html.H4(children = 'Ranking of the most insulted celebrities among those entered by the user' ),
                                        generate_table(datafram)])

        ],fluid = True, style = {'backgroundcolor' : '#F2DFCE', 'textAlign' : 'center'}
        )
        return layout

    app.layout = generate_layout()

    port = 8050
    def open_browser():
        webbrowser.open_new("http://localhost:{}".format(port))
    
    Timer(1,open_browser).start()
    app.run_server(debug=False)
