#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:11:16 2019

@author: rochet
"""

def bar_graph(data, bar_color):
    return {
                'data': [
                     {'y': [k for k, _ in sorted(zip(data.values(), data.keys()), reverse=True)],
                    'x': [v for _, v in sorted(zip(data.values(), data.keys()), reverse=True)],
                    'type': 'bar',
                    'textposition':"outside",
                    'marker':{
                            'color':'rgba(50, 171, 96, 0.6)',
                            'line':{
                                'color':'rgba(50, 171, 96, 1.0)',
                                'width':'1'},
                        },
                    'orientation':'v'}
                ],
                'layout': {
                    'text': 'percent'
                }
            }