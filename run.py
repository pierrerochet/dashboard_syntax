from dash.dependencies import Input, Output, State

# internes packages
from graph import bar_graph
import database
import layout_config
import statistic

# Config
app, app_layout = layout_config.config()


@app.callback(
    [Output('token_total', 'children'),
     Output('token_unique', 'children'),
     Output('nb_sentence', 'children'),
     Output('pos-graph', 'figure'),
     Output('dep-graph', 'figure'),
     Output('statistic_pos_tag', 'options'),
     Output('resultat_stats','children')],
    [Input('upload-data', 'contents'),
     Input('size_file', 'value'),
     Input('type_calcul_statistic', 'value'),
     Input('statistic_pos_tag','value')])
def update_data(content, size_file, type_calcul_statistic,statistic_pos_tag):
    if not content:
        return ["-", "-", "-", {}, {}, [], []]

    decoded = database.load(content)
    start_percentage_size, end_percentage_size = size_file
    dataset = database.create(decoded, start_percentage_size, end_percentage_size)
    g_stats, pos_stats, dep_stats, pos_tag_list = statistic.data_general_stats(dataset)
    pos_graph = bar_graph(pos_stats, 'rgba(50, 171, 96, 0.6)')
    dep_graph = bar_graph(dep_stats, '#95addd')
    total_token = g_stats["total"]
    diversity_token = g_stats["diversity"]
    total_sentence = g_stats["sentence"]

    calcul_statistic = update_statistic(type_calcul_statistic,statistic_pos_tag,pos_stats)

    return total_token, diversity_token, total_sentence, pos_graph, dep_graph, pos_tag_list, calcul_statistic


# version test
def update_statistic(value, pos_tag_choisi, data_pos_tag):
    if value == "moyenne":
        return statistic.moyenne(pos_tag_choisi, data_pos_tag)

    elif value == "ecart_type":
        return statistic.ecart_type(pos_tag_choisi, data_pos_tag)


if __name__ == '__main__':
    app.run_server(debug=True)
