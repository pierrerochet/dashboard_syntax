#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:11:16 2019

@author: rochet
"""
import numpy as np
import base64

def load(file):
    _ , content_string = file.split(',')
    decoded = base64.b64decode(content_string)
    return decoded.decode("UTF8")

def create(content,size_file):
    # file's percentage
    content = content[0:int(len(content)*size_file)]

    database = []
    save = {"form":[], "lemma":[], "pos":[], "dep":[], "size":0}
    input_file = content.split("\n")
    for l in input_file:
        if l !="":
            if "# sent_id" in l: save['sent_id'] = l[12:]
            elif "# text" in l: save['text'] = l[9:]
            else:
                try:
                    elements = l.split('\t')
                    save['form'].append(elements[1])
                    save['lemma'].append(elements[2])
                    save['pos'].append(elements[3])
                    save['dep'].append(elements[7])
                    save['size'] += 1
                except IndexError:
                    continue
        else:
            database.append(save)
            save = {"form":[], "lemma":[], "pos":[], "dep":[], "size":0}
    return database


def stats(database):
    pos_stats = {}
    dep_stats = {}
    total_sentence = 0
    seq_num_token = []
    seq_token = []
    for seq in database:
        total_sentence += 1
        seq_num_token.append(seq["size"])
        seq_token += seq["form"]
        for pos in seq["pos"]:
            pos_stats[pos] = pos_stats.get(pos, 0) + 1
        for dep in seq["dep"]:
            dep_stats[dep] = dep_stats.get(dep, 0) + 1
    diversity_token = len(set(seq_token))
    total_token = sum(seq_num_token)
    mean_token = np.mean(np.array(seq_num_token))
    std_token = np.std(np.array(seq_num_token))
    std_token = "{:.2f}".format(std_token)
    
    g_stats = {"total":total_token,"diversity":diversity_token,"mean":mean_token,"std":std_token, "sentence":total_sentence}# "size_file": size_file }
    return g_stats, pos_stats, dep_stats