#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html


def config():
    app = dash.Dash(__name__)
    app.layout = html.Div(id="page", children=[
        # HEADER ==================================================================
        html.Header(
            children=[html.Div([
                html.H2("Syntax Statistics"),
                html.P(id="text-usage", children="dashboard for conll format")
            ])]),
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
                                           'weigth': '100%'
                                       })]),
                        html.Label('Select size'),
                        dcc.RangeSlider(id="size_file",
                                        min=0,
                                        max=1,
                                        step=0.25,
                                        value=[0, 1],
                                        marks={0: "0", 0.25: "25%", 0.50: "50%", 0.75: '75%', 1: '100%'},
                                        allowCross=False)])]),

                # STATS GENERAL CADRE ============================================
                html.Div(className="cadre-left", children=[
                    html.Div(className="head-cadre", children=[
                        html.P('General Statistics')]),
                    html.Div(className="content-cadre", children=[
                        html.Div([], style={'width': '100%'})]),
                    dcc.Dropdown(id="statistic_pos_tag",
                                 value="",
                                 multi=False,
                                 ),
                    dcc.RadioItems(id="type_calcul_statistic",
                                   options=[
                                       {'label': 'Moyenne', 'value': 'moyenne'},
                                       {'label': 'Ecart-Type', 'value': 'ecart_type'},
                                       {'label': "Variance", "value": "variance"}
                                   ],
                                   value='',
                                   labelStyle={'display': 'inline-block'}
                                   ),
                        html.P(id="resultat_stats")

                            ])]),

            # MIDDLE FRAME ========================================================
            html.Div([
                html.Div(className="mid-frame", children=[
                    # FIRST HORIZONTAL FRAME ======================================
                    html.Div(className="large-hor-frame", children=[
                        html.Div(className="small-frame", children=[
                            html.Div(className="basic-cadre", children=[
                                html.Div(html.H4("Tokens")),
                                html.Div(className="number-cadre", id="token_total")])]),
                        html.Div(className="small-frame-mid", children=[
                            html.Div(className="basic-cadre", children=[
                                html.Div(html.H4("Unique Tokens")),
                                html.Div(className="number-cadre", id="token_unique")])]),
                        html.Div(className="small-frame", children=[
                            html.Div(className="basic-cadre", children=[
                                html.Div(html.H4("Sentences")),
                                html.Div(className="number-cadre", id="nb_sentence")])])]),

                    # GRAPH ZONE ==================================================
                    html.Div(className="graph-frame", children=[
                        dcc.Tabs(id="tabs", children=[
                            # GRAPH 1 : pos disparity =============================
                            dcc.Tab(label='POS disparity', children=[
                                html.Div([
                                    dcc.Graph(
                                        id='pos-graph',
                                        figure={})])]),
                            # GRAPH 2 : dep disparity =============================
                            dcc.Tab(label='DEP disparity', children=[
                                html.Div([
                                    dcc.Graph(
                                        id='dep-graph',
                                        figure={})])])])]),

                                    dcc.Graph(id="curve_graph",
                                              figure={})
                            ])])])])

    return app, app.layout
