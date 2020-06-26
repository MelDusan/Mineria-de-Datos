# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assumes you have a "wide-form" data frame with no index
# see https://plotly.com/python/wide-form/ for more options
df = pd.DataFrame({"x": [1, 2, 3], "freeCodeCamp/freeCodeCamp": [300000, 1, 2], "facebook/react": [140000, 4, 5], "tensorflow/tensorflow": [135000, 6, 7], "okFoundation/free-programming-books": [130000, 9, 10], "sindresorhus/awesome": [128000, 12, 13], "getify/You-Dont-Know-Js": [110000, 15, 16], "robbyrussell/oh-my-zsh": [90000, 18, 19], "kamranahmedse/developer-roadmap": [80000, 21, 22], "jwasham/coding-interview-university": [80000, 24, 25], "microsoft/vscode": [75000, 27, 28]})

fig = px.bar(df, x="x", y=["freeCodeCamp/freeCodeCamp", "facebook/react", "tensorflow/tensorflow", "okFoundation/free-programming-books", "sindresorhus/awesome", "getify/You-Dont-Know-Js", "robbyrussell/oh-my-zsh", "kamranahmedse/developer-roadmap", "jwasham/coding-interview-university", "microsoft/vscode"], barmode="group")

fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sistema de Recomendaciones para repositorios Github',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: Una aplicacion web para Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)