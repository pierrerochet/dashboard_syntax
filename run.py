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
     Output('statistic', 'options')],
    [Input('upload-data', 'contents'),
     Input('size-file', 'value'),
     Input('type_statistic', 'value')])
def update_data(content, value, type_statistic):
    if not content:
        return ["-", "-", "-", {}, {}, []]

    decoded = database.load(content)
    start_percentage_size, end_percentage_size = value
    dataset = database.create(decoded, start_percentage_size, end_percentage_size)
    g_stats, pos_stats, dep_stats, pos_tag_list = database.stats(dataset)
    pos_graph = bar_graph(pos_stats, 'rgba(50, 171, 96, 0.6)')
    dep_graph = bar_graph(dep_stats, '#95addd')
    total_token = g_stats["total"]
    diversity_token = g_stats["diversity"]
    total_sentence = g_stats["sentence"]

    return total_token, diversity_token, total_sentence, pos_graph, dep_graph, pos_tag_list


# version test
def update_statistic(value, data):
    if value == "moyenne":
        statistic.moyenne(data)

    elif value == "ecart_type":
        pass


if __name__ == '__main__':
    app.run_server(debug=True)
