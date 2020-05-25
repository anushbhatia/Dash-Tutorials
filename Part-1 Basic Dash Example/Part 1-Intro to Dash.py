import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[html.H1('Welcome to Dash'),
                                dcc.Graph(id="example",
                                          figure= {
                                                  'data':[{
                                                          'x':[1,2,3,4,5],
                                                          'y':[5,4,1,3,1],
                                                           'type':'line',
                                                           'name':'Anush Plot',
                                                          },{'x':[1,2,3,4,5],
                                                          'y':[7,8,4,5,2],
                                                           'type':'bar',
                                                           'name':'Car Plot',
                                                           }],
                                                    'layout':{
                                                            'title':'Basic Graph'}
                                                  }
                                          )])
if __name__ == '__main__':
    app.run_server()
