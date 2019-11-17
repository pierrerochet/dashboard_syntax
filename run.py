import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
#import plotly.graph_objects as go

# internes packages
from graph import bar_graph
import database

external_stylesheets = ["static/css/main.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(id="page", children=[
    # HEADER ==================================================================
    html.Header(
        children=[html.Div([
            html.H2("Syntax Statistics"),
            html.P(id="text-usage", children="dashboard for conll format")
            ]) ]),
    # BODY ====================================================================
    html.Div(id="body", children=[
        # LEFT COLUMN =========================================================
        html.Div(className="column-left", children=[
            # CONFIG CADRE ====================================================
            html.Div(className="config", children=[
                html.Div(className="cadre-config", children=[
                    html.P(children=['Select conll file']),
                    html.Hr(className='hr'),
                    html.Div(className='load-file', children=[
                        dcc.Upload(id='upload-data', children=
                            html.Div(['Upload File']),
                            style={
                                'lineHeight': '100px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'weigth':'100%'
                                    }) ]),
                    html.Label('Select size'),
                    dcc.Slider(id="size-file",
                        min=0,
                        max=4,
                        marks={0:"0", 1:"0.25", 2:"0.50", 3:'0.75', 4:'1'},
                        value=4) ]) ]),
            # STATS GENERAL CADRE =============================================
            html.Div(className="cadre-left", children=[
                html.Div(className="head-cadre", children=[
                    html.P('General Statistics') ]),
                html.Div(className="content-cadre", children=[
                    html.Div([ ], style={'width':'100%'}) ]) ]) ]),


        # MIDDLE FRAME ========================================================
        html.Div([
            html.Div(className="mid-frame", children=[
                # FIRST HORIZONTAL FRAME ======================================
                html.Div(className="large-hor-frame", children=[
                    html.Div(className="small-frame", children=[
                        html.Div(className="basic-cadre", children=[
                            html.Div(html.H4("Tokens")),
                            html.Div(className="number-cadre" ,id="token_total") ]) ]),
                    html.Div(className="small-frame-mid", children=[
                        html.Div(className="basic-cadre",children=[
                            html.Div(html.H4("Unique Tokens")),
                            html.Div(className="number-cadre", id="token_unique") ]) ]),
                    html.Div(className="small-frame", children=[
                        html.Div(className="basic-cadre",children=[
                            html.Div(html.H4("Sentences")),
                            html.Div(className="number-cadre", id="nb_sentence") ]) ]) ]),
                    

                # GRAPH ZONE ==================================================
                html.Div(className="graph-frame", children=[
                    dcc.Tabs(id="tabs", children=[
                        # GRAPH 1 : pos disparity =============================
                        dcc.Tab(label='POS disparity', children=[
                            html.Div([
                                dcc.Graph(
                                    id='pos-graph',
                                    figure={} ) ]) ]),
                        # GRAPH 2 : dep disparity =============================
                        dcc.Tab(label='DEP disparity', children=[
                            html.Div([
                                dcc.Graph(
                                    id='dep-graph',
                                    figure={} ) ]) ]) ]) ]) ]) ]) ]) ])


@app.callback(
    [Output('token_total', 'children'),
     Output('token_unique', 'children'),
     Output('nb_sentence', 'children'),
     Output('pos-graph', 'figure'),
     Output('dep-graph', 'figure')],
    [Input('upload-data', 'contents'),
    Input('size-file', 'marks'),
    Input('size-file', 'value')])
def update_data(content, marks, value):
    if not content:
        return ["-", "-", "-", {}, {}]
    decoded = database.load(content)
    size_file = float(marks[str(value)])
    dataset = database.create(decoded,size_file)
    
    g_stats, pos_stats, dep_stats = database.stats(dataset)
    pos_graph = bar_graph(pos_stats, 'rgba(50, 171, 96, 0.6)')
    dep_graph = bar_graph(dep_stats, '#95addd')
    total_token = g_stats["total"]
    diversity_token = g_stats["diversity"]
    total_sentence = g_stats["sentence"]
    return total_token, diversity_token, total_sentence, pos_graph, dep_graph


if __name__ == '__main__':
    app.run_server(debug=True)