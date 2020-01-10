#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

def config():
    app = dash.Dash(__name__, suppress_callback_exceptions=True)

    app.layout = html.Div(id='page', children=[
        dcc.Location(id='url', refresh=True),
        # HEADER ==================================================================
        html.Header(
            children=[html.Div([
                html.H2('Syntax Statistics'),
                html.P(id='text-usage', children='dashboard for conll format')
            ])]),
        # BODY ====================================================================
        html.Div(id='body', children=[
            html.Div(className='large-frame', children=[
                # LEFT COLUMN =====================================================
                html.Div(className='column-left', children=[
                    # CONFIG CADRE ================================================
                    html.Div(className='config', children=[
                        html.Div(className='cadre-config', children=[
                            html.P(children=['Select conll file']),
                            html.Hr(className='hr'),
                            html.Div(className='load-file', children=[
                                dcc.Upload(id='upload-data',  children=
                                html.Div(['Upload File']),
                                           style={
                                               'lineHeight': '100px',
                                               'borderWidth': '1px',
                                               'borderStyle': 'dashed',
                                               'borderRadius': '5px',
                                               'textAlign': 'center',
                                               'weigth': '100%'
                                           },
                                           multiple=None)]),
                            html.Label('Select size'),
                            dcc.RangeSlider(id='size_file',
                                            min=0,
                                            max=1,
                                            step=0.25,
                                            value=[0, 1],
                                            marks={0: '0', 0.25: '25%', 0.50: '50%', 0.75: '75%', 1: '100%'},
                                            allowCross=False)])]),
                    # STATS GENERAL CADRE =========================================
                    html.Div(className='cadre-left', children=[
                        html.Div(className='head-cadre', children=[
                            html.P('General Statistics')]),
                        html.Br(),
                        html.Div(className='content-cadre', children=[
                            dcc.Dropdown(id='statistic_pos_tag',
                                         value='',
                                         multi=False,
                                         placeholder='Choose a POS tag',
                                         disabled=False,
                                         persistence=False ),
                            dcc.RadioItems(id='calculation_type',
                                           options=[
                                               {'label': 'Mean', 'value': 'mean'},
                                               {'label': 'Standard deviation', 'value': 'std'},
                                               {'label': 'Variance', 'value': 'variance'}],
                                           value='',
                                           labelStyle={'display': 'inline-block'}),
                            html.Br(),
                            html.P(id='result_stats', children=[]),
                        ])]),
                ]),
                # MIDDLE FRAME ====================================================
                html.Div([
                    html.Div(className='mid-frame', children=[
                        # FIRST HORIZONTAL FRAME ==================================
                        html.Div(className='large-hor-frame', children=[
                            html.Div(className='small-frame', children=[
                                html.Div(className='basic-cadre', children=[
                                    html.Div(html.H4('Tokens')),
                                    dcc.Loading(type='dot', children=[
                                        html.Div(className='number-cadre', id='token_total')])])]),
                            html.Div(className='small-frame-mid', children=[
                                html.Div(className='basic-cadre', children=[
                                    html.Div(html.H4('Unique Tokens')),
                                    dcc.Loading(type='dot', children=[
                                        html.Div(className='number-cadre', id='token_unique')])])]),
                            html.Div(className='small-frame', children=[
                                html.Div(className='basic-cadre', children=[
                                    html.Div(html.H4('Sentences')),
                                    dcc.Loading(type='dot', children=[
                                        html.Div(className='number-cadre', id='nb_sentence')])])])]),

                        # GRAPH ZONE ==============================================
                        html.Div(className='graph-frame', children=[
                            dcc.Tabs(id='tabs', children=[
                                # GRAPH 1 : pos disparity =========================
                                dcc.Tab(label='POS disparity', children=[
                                    html.Div([
                                        dcc.Loading(type='dot', children=[dcc.Graph(
                                            id='pos-graph',
                                            figure={})])])]),
                                # GRAPH 2 : dep disparity =========================
                                dcc.Tab(label='DEP disparity', children=[
                                    html.Div([
                                        dcc.Graph(
                                            id='dep-graph',
                                            figure={})])])])])])])]),
            html.Div([
                # RELATION TABLE ZONE ===============================================
                html.Div(className='large-box', children=[
                    html.Div(className='head-large-box', children=[
                        html.H3('Relations table'),
                        html.Button('Generate relations table', id='button-generate-rel_table',n_clicks=0)
                    ]),
                    # TABLE : specificity
                    html.Div(className='content-box', children=[
                        dcc.Loading(type='dot', children=[
                            html.Div(id='frame-table-rel', children=[])])])]),

                # TABLE PHRASE ZONE ===============================================
                html.Div(className='large-box', children=[
                    html.Div(className='head-large-box', children=[
                        html.H3('Sentences')
                    ]),
                    # TABLE : specificity
                    html.Div(className='content-box', children=[
                        # TABLE : List trees
                        dcc.Loading(type='dot', children=[
                            html.Div(id='frame-table-list',children=[])
                        ])])]),
                # QUICK EDIT TREE ZONE =============================================
                html.Div(id='quick-edit-frame', className='large-box', children=[
                    html.Div(className='head-large-box', children=[
                        html.H3('Quick Edit Tree')
                    ]),
                    html.Div(id='quick-edit', className='content-box', children=[
                        html.Div(id='head-quick-edit', children=[
                            dcc.Dropdown(id='loading-tree', options=[],
                                         optionHeight=80,
                                         placeholder='Select a sentence'),
                            html.Div(id='quick-edit-function', children=[
                                html.Button('Reset', id='reset-button', n_clicks=0),
                                html.Button('Add node :', id='editing-rows-button', n_clicks=0),
                                dcc.Input(id='input-node-index', type='number', debounce=True,
                                          placeholder='Enter node index', value=''),
                                html.Div(id='save-frame', children=[
                                    html.Button('Save tree', id='save-tree-button', n_clicks=0),
                                    html.Div(id='confirm-frame')])])]),

                        # edit table
                        dcc.Loading(type='dot', children=[
                            html.Div(id='frame-tree', className='large-frame',
                                     style={'heigth': '100%', 'width': '500px'},
                                     children=[])])])]),
                # EXPORT ZONE =======================================================
                html.Div(id='export-frame', className='large-box', children=[
                    html.H3('Export a new conllu file'),
                    dcc.Input(id='input-name', type='text',
                              placeholder='Enter a name...',
                              value=''),
                    html.Button('Export', id='button-export'),
                    html.Div(id='frame-export-link')
                ])
            ])])
            ])

    return app, app.layout

