import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import webbrowser
from threading import Timer

def appli(datafram) : 
    datafram = datafram.sort_values(by=['frequency'], ascending = False)
    markdown_text = '''
    ### Swear words detector
    Interactive dashboard providing some statistics to analyse harassment on Twitter
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
        html.Label('Number of tweets downloaded'),
        html.H4(children='Ranking of the most insulted celebrities among those entered by the user'),
        generate_table(datafram)])
    port = 8050
    def open_browser():
        webbrowser.open_new("http://localhost:{}".format(port))
    
    Timer(1,open_browser).start()
    app.run_server(debug=False)
    
