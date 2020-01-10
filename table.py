#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_table


# pour afficher un tableau vide (on va l'utiliser pour nettoyer les tableaux à chaque upload)
def empty(value):
    return dash_table.DataTable(id=value)


# table relation
def rel_table(data_table, columns_table):
     return dash_table.DataTable(
                                id='table-rel',
                                style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                               'fontWeight': 'bold'},
                                style_cell={'textAlign': 'center',
                                             'width':'130px',
                                             'textOverflow': 'ellipsis'},
                                 style_table={'width': '100%',
                                            'minWidth': '100%'
                                              },


                                fixed_rows={'headers': True, 'data': 0 },
                                fixed_columns={'headers': True, 'data': 2},
                                style_data_conditional=[
                                         {'if': {'row_index': 'odd'},
                                          'backgroundColor': 'rgb(248, 248, 248)'},
                                         {'if':{'column_id': 'node'},
                                         'backgroundColor': '#3D9970',
                                         'color': 'white',
                                         'width':'50px'},
                                         {'if':{'column_id': 'head'},
                                         'backgroundColor': '#8f99ed',
                                         'color': 'white',
                                         'width':'50px'}
                                        ],
                                columns=columns_table,
                                data=data_table)


# table phrase
def list_table(data_table, columns_table):
     return dash_table.DataTable(id='table-list',
                                 style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                               'fontWeight': 'bold'},
                                 style_cell={'textAlign': 'left', 'min-width':'50px'},
                                 style_data_conditional=[{'if':{'column_id': 'ind'},
                                                        'backgroundColor': 'rgb(230, 230, 230)',

                                                          'fontWeight': 'bold',
                                                         'textAlign': 'center',
                                                         'width':'50px'}
                                                         ],
                                 style_table={'max-height': '350px',
                                              'width': '100%',
                                              'minWidth': '100%'
                                              },
                                 fixed_rows={'headers': True, 'data': 0 },
                                 columns=columns_table,
                                 data=data_table)


# edit table
def quick_edit_table(data_table, columns_table, data_dropdown):
    return dash_table.DataTable(
        id='table-tree',
        dropdown=data_dropdown,
        # fixed_rows={'headers': True, 'data': 0 },
        row_deletable=True,
        editable=True,
        columns=columns_table,
        data=data_table,
        style_cell={'textAlign': 'left', 'textOverflow': 'ellipsis'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
        style_data_conditional=[{'if': {'column_id': 'index'},
                                 'backgroundColor': 'rgb(230, 230, 230)',
                                 'textAlign': 'center',
                                 'fontWeight': 'bold',
                                 'editable': False}],
        style_table={
            'height': '500px',
            'width': '100%',
            'overflowY': 'scroll',
            'overflowX': 'scroll'})
