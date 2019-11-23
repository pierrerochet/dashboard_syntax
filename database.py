#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import base64


def load(file):
    _, content_string = file.split(',')
    decoded = base64.b64decode(content_string)
    return decoded.decode("UTF8")


def create(content, start_percentage_size, end_percentage_size):
    database = []
    count_phrase = 0
    save = {"form": [], "lemma": [], "pos": [], "dep": [], "size": 0, "phrase_id": count_phrase}
    input_file = content.split("\n")
    for l in input_file:
        if l != "":
            if "# sent_id" in l:
                save['sent_id'] = l[12:]

            elif "# text" in l:
                save['text'] = l[9:]

                count_phrase += 1
                save['phrase_id'] = count_phrase

            else:
                elements = l.split('\t')
                save['form'].append(elements[1])
                save['lemma'].append(elements[2])
                save['pos'].append(elements[3])
                save['dep'].append(elements[7])
                save['size'] += 1
        else:
            database.append(save)
            save = {"form": [], "lemma": [], "pos": [], "dep": [], "size": 0, "phrase_id": count_phrase}

    ## percentage's file ##
    database_sized = percentage_file(database, start_percentage_size, end_percentage_size, count_phrase)

    return database_sized


def percentage_file(database, start_percentage_size, end_percentage_size, count_phrase):
    start_percentage_size *= count_phrase
    end_percentage_size *= count_phrase

    database_sized = database[int(start_percentage_size):int(end_percentage_size)]

    return database_sized


def pos_tag_extraction(data):
    resultat = []
    dico = {}
    for x, y in zip(data.values(), data.keys()):
        dico["label"] = x
        dico["value"] = y
        resultat.append(dico)
        dico = {}

    return resultat


def stats(database_sized):
    pos_stats = {}
    dep_stats = {}
    total_sentence = 0
    pos_tag = {}
    seq_num_token = []
    seq_token = []

    for seq in database_sized:
        total_sentence += 1
        seq_num_token.append(seq["size"])
        seq_token += seq["form"]
        for pos in seq["pos"]:
            pos_stats[pos] = pos_stats.get(pos, 0) + 1
            pos_tag.setdefault(pos, pos)
        for dep in seq["dep"]:
            dep_stats[dep] = dep_stats.get(dep, 0) + 1

    pos_tag_list = pos_tag_extraction(pos_tag)
    diversity_token = len(set(seq_token))
    total_token = sum(seq_num_token)
    mean_token = np.mean(np.array(seq_num_token))
    std_token = np.std(np.array(seq_num_token))
    std_token = "{:.2f}".format(std_token)

    g_stats = {"total": total_token, "diversity": diversity_token, "mean": mean_token, "std": std_token,
               "sentence": total_sentence}
    return g_stats, pos_stats, dep_stats, pos_tag_list
