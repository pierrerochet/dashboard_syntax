#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def mean(dict_stats, statistic_values):
    return np.mean(dict_stats[statistic_values])


def variance(dict_stats, statistic_values):
    return np.var(dict_stats[statistic_values])


def std(dict_stats, statistic_values):
    return np.std(dict_stats[statistic_values])
