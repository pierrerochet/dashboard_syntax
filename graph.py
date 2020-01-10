#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:11:16 2019

@author: rochet
"""

def bar_graph(data, bar_color):
    data_sorted = sorted(zip(data.values(), data.keys()), reverse=True)
    return {'data': [
                     {'y': [k for k, _ in data_sorted],
                    'x': [v for _, v in data_sorted],
                    'type': 'bar',
                    'textposition':"outside",
                    'marker':{
                            'color': bar_color,
                            'line':{
                                'color':'rgba(50, 171, 96, 1.0)',
                                'width':'1'} },
                    'orientation':'v'} ],
            'layout': { 'text': 'percent' } }
