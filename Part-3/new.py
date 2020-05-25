import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import random
import plotly
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id="live-graph", animate=True),
    dcc.Interval(
        id='graph-update',
        interval=2000,
        n_intervals=0
    )
])
@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))
    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )
    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(Y)]),
                                                yaxis=dict(range=[min(X), max(Y)]))}


if __name__ == '__main__':
    app.run_server()
