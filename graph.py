#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bar_graph(data, bar_color):
    return {
        'data': [
            {'y': [sum(k) for k, _ in sorted(zip(data.values(), data.keys()), reverse=True)],
             'x': [v for _, v in sorted(zip(data.values(), data.keys()), reverse=True)],
             'type': 'bar',
             'textposition': "outside",
             'marker': {
                 'color': bar_color,
                 'line': {
                     'color': 'rgba(50, 171, 96, 1.0)',
                     'width': '1'},
             },
             'orientation': 'v'}
        ],
        'layout': {
            'text': 'percent'
        }
    }


def curve_graph(data, bar_color):
    return {
        'data' : [
                        {
                                    'x' : [sum(k) for k, _ in sorted(zip(data.values(), data.keys()), reverse=True)],
                                    'y' : [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                       350, 430, 474, 526, 488, 537, 500, 439],
                                    'name' : 'Rest of world',
                                    'marker' : {
                                        'color': bar_color
                                    }
                                }
                            ],
                            'layout': {
                                'title':'US Export of Plastic Scrap',
                                'showlegend': 'True',
                                'legend':{
                                    'x':'0',
                                    'y':'1.0'
            }
    },
                'margin' : {'l':40, 'r':0, 't':40, 'b':30},
                        'style' : {'height': 300},
                        'id':'my-graph'}
