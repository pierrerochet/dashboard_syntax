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

    # percentage's file #
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


def array_data(database_sized, pos_tag, dep_tag):
    pos_stats = {}
    dep_stats = {}

    # array for pos_tag and dependencies
    bags_deps = []
    bag_deps = np.zeros(len(list(dep_tag.values())))

    bags_pos_tag = []
    bag_pos_tag = np.zeros(len(list(pos_tag.values())))

    for seq in database_sized:
        for i, word in enumerate(list(dep_tag.values())):
            for dep in seq["dep"]:
                if dep == word:
                    bag_deps[i] += 1

        bags_deps.append(bag_deps)
        bag_deps = np.zeros(len(list(dep_tag.values())))

        for i, word in enumerate(list(pos_tag.values())):
            for pos in seq["pos"]:
                if pos == word:
                    bag_pos_tag[i] += 1

        bags_pos_tag.append(bag_pos_tag)
        bag_pos_tag = np.zeros(len(list(pos_tag.values())))

    # creation dico for pos_stats and dep_stats from the arrays
    etape_par_etape = []
    for index, value in enumerate(pos_tag.values()):
        for element in bags_pos_tag:
            etape_par_etape.append(element[index])

        pos_stats[value] = etape_par_etape
        etape_par_etape = []

    for index, value in enumerate(dep_tag.values()):
        for element in bags_deps:
            etape_par_etape.append(element[index])

        dep_stats[value] = etape_par_etape
        etape_par_etape = []

    return pos_stats, dep_stats
