#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import send_file, request
import io

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

# internal packages
from graph import bar_graph
from table import rel_table, list_table, quick_edit_table, empty
from database import treebank
from layout_config import config
from statistic import mean, variance, std

app, app_layout = config()

# update when upload file
@app.callback(
    [Output('token_total', 'children'),
     Output('token_unique', 'children'),
     Output('nb_sentence', 'children'),
     Output('pos-graph', 'figure'),
     Output('dep-graph', 'figure'),
     Output('loading-tree', 'options'),
     Output('statistic_pos_tag','options'),
     Output('frame-table-rel', 'children'),
     Output('table-rel', 'active_cell'),
     Output('resultat_stats','children')],
    [Input('upload-data', 'contents'),
     Input('size_file', 'value'),
     Input('button-generate-rel_table', 'n_clicks'),
     Input('type_calcul_statistic', 'value'),
     Input('statistic_pos_tag', 'value')
     ])
def update_data(contents, size_file, n_clicks, type_stats, statistic_values):
    if contents is None:
        return ['-', '-', '-', {}, {}, [],[],[],[],[]]

    # corpus size
    start_percentage_size, end_percentage_size = size_file

    # treebank object
    global tb
    tb = treebank(contents, start_percentage_size, end_percentage_size)

    # getting informations
    pos_stats = tb.lex_pos
    dep_stats = tb.lex_dep
    pos_graph = bar_graph(pos_stats, '#8f99ed')
    dep_graph = bar_graph(dep_stats, '#3D9970')
    total_token = tb.sum_nodes
    diversity_token = len(tb.lex_form.keys())
    total_sentence = tb.sum_trees
    load_option = [{'label': s, 'value': s} for s in tb.lex_sent]

    # statistics pos tags
    pos_tag_list = [{'label': x, 'value': x} for x in tb.lex_pos.keys()]
    dict_stats = tb.dict_stats # on recupere un array pour pouvoir calculer facilement avec numpy
    result_stats = update_statistic(dict_stats,type_stats, statistic_values)

    # clear relation table when upload file
    rel_t = generate_rel_table(n_clicks)
    #  clear sentence list when upload file
    active_cell_table_list = None

    return total_token, diversity_token, total_sentence, pos_graph, dep_graph, load_option, pos_tag_list, rel_t, active_cell_table_list, result_stats

# Generate relation table
def generate_rel_table(n_clicks):
    # check corpus size and upload corpus
    context = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    if context == 'button-generate-rel_table':
        if n_clicks > 0:

            # relations table
            columns = [{'id': 'node', 'name': 'NODE'},
                       {'id': 'head', 'name': 'HEAD'}]
            columns += [{'id': n, 'name': n, 'hideable': True} for n in tb.lex_dep]
            data = tb.rel_clus['pos']
            rel_t = rel_table(data, columns)
            return rel_t

    elif context == 'upload-data' or 'size_file':
        return empty('table-rel')


# to update statistic 
def update_statistic(dict_stats,type_stats, statistic_values):
    try:
        if type_stats == 'moyenne':
            return 'Résultat : {:.2f}'.format(mean(dict_stats, statistic_values))
        elif type_stats == 'variance':
            return 'Résultat : {:.2f}'.format(variance(dict_stats, statistic_values))
        elif type_stats == 'ecart_type':
            return 'Résultat : {:.2f}'.format(std(dict_stats, statistic_values))
    except KeyError:
        return None


# visualization sentences
@app.callback(
    [Output('frame-table-list', 'children'),
     Output('table-list','active_cell')],
    [Input('table-rel', 'active_cell')],
    [State('table-rel', 'active_cell'),
     State('table-rel', 'data')])
def load_list_tree(data_timestamp, active_cell, data):
    # clear sentences table
    if active_cell is None:
        return empty('table-list'), None

    elif active_cell != None:
        if active_cell['column_id'] in data[active_cell['row']]:
            n = data[active_cell['row']]['node']
            h = data[active_cell['row']]['head']
            d = active_cell['column_id']
            for ele in tb.rel_index['pos']:
                if ele['node'] == n and ele['head'] == h:
                    list_index = ele[d]
            list_sent = []
            for sent in tb.lex_sent:
                if tb.lex_sent.index(sent) in list_index:
                    list_sent.append(sent)
            columns = [{'id': 'ind', 'name': 'index'},
                       {'id': 'sent', 'name': 'Sentences'}]
            data = [{'sent': list_sent[ind], 'ind': ind + 1} for ind in range(len(list_sent))]
            return list_table(data, columns), None
        else:
            return empty('table-list'), None


# display tree
@app.callback(
    [Output('frame-tree', 'children'),
    Output('save-tree-button', 'n_clicks')],
    [Input('loading-tree', 'value')])
def loading_table_tree(value_sent):


    global count_saved_tree
    count_saved_tree = 0
    if value_sent is None:
        return empty('table-tree'), count_saved_tree
    
    elif value_sent != None:
        columns_table = [{'id': 'index', 'name': 'index'},
                         {'id': 'form', 'name': 'form'},
                         {'id': 'lemma', 'name': 'lemma'},
                         {'id': 'pos', 'name': 'pos', 'presentation': 'dropdown'},
                         {'id': 'dep', 'name': 'dep', 'presentation': 'dropdown'},
                         {'id': 'head', 'name': 'head'}]
        for t in tb.trees:
            if t.sent == value_sent:
                data_table = t.to_list()
                data_dropdown = {'pos': {'options': [{'label': pos, 'value': pos} for pos in sorted(tb.lex_pos)]},
                         'dep': {'options': [{'label': dep, 'value': dep} for dep in sorted(tb.lex_dep)]}}
                return quick_edit_table(data_table, columns_table, data_dropdown), count_saved_tree


@app.callback(
    Output('loading-tree', 'value'),
    [Input('table-list', 'active_cell'),
     Input('reset-button','n_clicks')],
    [State('table-list', 'active_cell'),
     State('table-list', 'data')])
def visualize(reset_button, data_timestamp,active_cell, data):
    if active_cell != None or reset_button != None:
        sent = data[active_cell['row']]['sent']
        return sent


@app.callback(
    [Output('table-tree', 'data'),
     Output('input-node-index', 'value')],
    [Input('editing-rows-button', 'n_clicks')],
    [State('table-tree', 'data'),
     State('table-tree', 'columns'),
     State('input-node-index', 'value')])
def add_node(n_clicks, rows, columns, index):
    if n_clicks > 0 and index != None and index != '':
        new_row = {'index': index}
        new_row.update({c['id']: '' for c in columns[1:]})
        for d in rows:
            if d['head'] != '':
                head = int(d['head'])
            else:
                head = -1
            ind = int(d['index'])
            if ind > index - 1:
                d['index'] = str(ind + 1)
            if head > index - 1:
                d['head'] = str(head + 1)
        rows.insert(index - 1, new_row)
    return [rows, '']


@app.callback(
    Output('confirm-frame', 'children'),
    [Input('save-tree-button', 'n_clicks')],
    [State('table-tree', 'data'),
     State('loading-tree', 'value')])
def save_tree(n_clicks, data, sent):
    if n_clicks > 0:
        for t in tb.trees:
            if t.sent == sent:
                t.edit(data)
                return 'saved'


@app.callback(
    Output('frame-export-link', 'children'),
    [Input('button-export', 'n_clicks')],
    [State('input-name', 'value')])
def update_link(n_clicks, name):
    if n_clicks != None:
        name += '.conllu'
        return html.A(name,
                        id='link-export',
                        target='_blank',
                        download=name,
                        href=f'/dash/export_file?name={name}')



@app.server.route('/dash/export_file')
def download():
    try:
        name = request.args.get('name')
        IO = io.BytesIO()
        IO.write(tb.export_trees_to_text().encode('utf8'))
        IO.seek(0)
        file = send_file(IO,
                         mimetype='text/plain',
                         attachment_filename=name,
                         as_attachment=True)
        return file
    except:
        return ''


if __name__ == '__main__':
    app.run_server(debug=True)
