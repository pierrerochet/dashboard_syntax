#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# internes packages
import database


def data_general_stats(database_sized):
    total_sentence = 0

    pos_tag = {}
    dep_tag = {}
    seq_num_token = []
    seq_token = []

    for seq in database_sized:
        total_sentence += 1
        seq_num_token.append(seq["size"])
        seq_token += seq["form"]

        for pos in seq["pos"]:
            pos_tag.setdefault(pos, pos)

        for dep in seq["dep"]:
            dep_tag.setdefault(dep, dep)

    pos_stats, dep_stats = database.array_data(database_sized, pos_tag, dep_tag)
    pos_tag_list = database.pos_tag_extraction(pos_tag)
    diversity_token = len(set(seq_token))
    total_token = sum(seq_num_token)

    mean_token = np.mean(np.array(seq_num_token))
    std_token = np.std(np.array(seq_num_token))
    std_token = "{:.2f}".format(std_token)

    g_stats = {"total": total_token, "diversity": diversity_token, "mean": mean_token, "std": std_token,
               "sentence": total_sentence}

    return g_stats, pos_stats, dep_stats, pos_tag_list


def moyenne(pos_tag_choisi, data_pos_tag):
    try:
        resultat = "Moyenne de {} : {:.2f}".format(pos_tag_choisi,np.mean(data_pos_tag[pos_tag_choisi]))
        return resultat

    except KeyError:
        return "Choisir un POS tag"


def ecart_type(pos_tag_choisi, data_pos_tag):
    try:
        resultat = "Ecart-type de {} : {:.2f}".format(pos_tag_choisi, np.std(data_pos_tag[pos_tag_choisi]))
        return resultat
    except KeyError:
        return "Choisir un POS tag"


def variance(pos_tag_choisi, data_pos_tag):
    try:
        resultat = "Variance de {} : {:.2f}".format(pos_tag_choisi, np.var(data_pos_tag[pos_tag_choisi]))
        return resultat
    except KeyError:
        return "Choisir un POS tag"

