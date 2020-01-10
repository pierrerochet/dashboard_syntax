#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import base64
import re
import numpy as np


class treebank:
    '''Created a treebank object'''
    def __init__(self, file,start_percentage_size, end_percentage_size):
        # lexiques
        self.lex_sent = []
        self.lex_form = {}
        self.lex_lemma = {}
        self.lex_pos = {}
        self.lex_dep = {}
        # dependencies clusters
        self.rel_clus = {'pos':[], 'form':[]}
        self.rel_index = {'pos':[], 'form':[]}
        # stats
        self.sum_trees = 0
        self.mean_trees = 0
        self.std_trees = 0
        self.sum_nodes = 0
        # content
        self.trees = []
        self.pos_tag_dict = {}
        self.bags_pos_tag = []
        self.etape_par_etape = []
        self.dict_stats = {}

        def load(file):
            _ , content_string = file.split(',')
            decoded = base64.b64decode(content_string)
            return decoded.decode('UTF8')

        def split_treebank(content_file, start_percentage_size, end_percentage_size):
            trees = re.split('\n{2,}', content_file)

            # taille de corpus
            start_percentage_size *= len(trees)
            end_percentage_size *= len(trees)
            trees_sized = trees[int(start_percentage_size):int(end_percentage_size)]

            return trees_sized

        # traitement et recuperation des données concernant notre fichier
        def update_rel_clus(t, i, attr):
            for n in t.nodes:
                self.pos_tag_dict[n.pos] = n.pos
                node = getattr(n, attr)
                dep = n.dep
                if n.head == 0: head = 'ROOT'
                else: head = getattr(t.nodes[int(n.head)-1], attr)
                # upgrade self.form_clus
                ind = 0
                upgrade = False
                for dict_rel in self.rel_clus[attr]:
                    if dict_rel['node'] == node and dict_rel['head'] == head:
                        dict_rel[dep] = dict_rel.get(dep, 0) + 1
                        merge_index = self.rel_index[attr][ind].get(dep, []) + [i]
                        self.rel_index[attr][ind][dep] = merge_index
                        upgrade = True
                        break
                    ind += 1
                if upgrade == False:
                    init_dict_rel = {'node':node, 'head':head, dep:1 }
                    init_dict_index = {'node':node, 'head':head, dep:[i] }
                    self.rel_clus[attr].append(init_dict_rel)
                    self.rel_index[attr].append(init_dict_index)

        # pour le calcul statistique, on recupere un sac de mots qui nous dit chaque phrase contient combien de pos tag.
        def array(self,trees_string):
            # sac de mots pour stats
            bag_pos_tag = np.zeros(len(list(self.lex_pos.keys())))

            for i in range(len(trees_string)):
                if trees_string[i] != '':
                    t = tree(trees_string[i])

                    for n in t.nodes:
                        for ind, element in enumerate(list(self.lex_pos.keys())):
                            if element == n.pos:
                                bag_pos_tag[ind] += 1

                self.bags_pos_tag.append(bag_pos_tag)
                bag_pos_tag = np.zeros(len(list(self.lex_pos.keys())))

            for index, value in enumerate(self.lex_pos.keys()):
                for element in self.bags_pos_tag:
                    self.etape_par_etape.append(element[index])

                self.dict_stats[value] = self.etape_par_etape
                self.etape_par_etape = []

            return self.dict_stats
                    
    
        treebank_string = load(file)
        trees_string = split_treebank(treebank_string, start_percentage_size, end_percentage_size)

        for i in range(len(trees_string)):

            if trees_string[i] != '':
                t = tree(trees_string[i])
                self.lex_sent.append(t.sent)
                self.sum_trees += 1
                self.trees.append(t)
                update_rel_clus(t, i, 'pos')

                for n in t.nodes:
                    self.sum_nodes += 1
                    self.lex_form[n.form] = self.lex_form.get(n.form, 0) + 1
                    self.lex_lemma[n.lemma] = self.lex_lemma.get(n.lemma, 0) + 1
                    self.lex_pos[n.pos] = self.lex_pos.get(n.pos, 0) + 1
                    self.lex_dep[n.dep] = self.lex_dep.get(n.dep, 0) + 1


        self.dict_stats = array(self,trees_string)
        sizes = np.array([tree.sum for tree in self.trees])
        self.mean_trees = np.mean(sizes)
        self.std_trees = np.std(sizes)

    def export_trees_to_text(self):
        '''Export a new conll file'''
        text = ''
        for t in self.trees:
            text += t.to_text() + '\n'
        return text


class tree:
    '''Created a tree object'''
    def __init__(self, tree_format):
        self.sent = ''
        self.nodes = []
        self.sum = 0
        nodes = tree_format.split("\n")
        for i in range(len(nodes)):
            n = nodes[i]
            if '# sent_id' not in n and '# text' not in n:
                index, form, lemma, pos, _, _, head, dep, _, _  = n.split('\t')
                self.sent += f'{form} ' 
                if "-" not in index: # for multiple index (du, des, lesquels, etc) 
                    self.nodes.append(node(index, form, lemma, pos, head, dep))
                    self.sum += 1
    
    def edit(self, nodes_list):
        nodes = []
        for e in nodes_list:
            n = node(e['index'],
                     e['form'],
                     e['lemma'],
                     e['pos'],
                     e['head'],
                     e['dep'])
            nodes.append(n)
        self.nodes = nodes
                    
    def to_list(self):
        '''Return the nodes tree in list of dictionnary'''
        nodes_list = []
        for n in self.nodes:
            node_dict = {}
            node_dict['index'] = n.index
            node_dict['form'] = n.form
            node_dict['lemma'] = n.lemma
            node_dict['pos'] = n.pos
            node_dict['dep'] = n.dep
            node_dict['head'] = n.head
            nodes_list.append(node_dict)
        return nodes_list
    
    def to_text(self):
        '''return the tree in text form'''
        text = ''
        for n in self.nodes:
            text += f'{n.index}\t{n.form}\t{n.lemma}\t{n.pos}\t{n.dep}\t{n.head}\n'
        return text


class node:
    '''Created a node object'''
    def __init__(self, index, form, lemma, pos, head, dep):
        self.index = index
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.dep = dep
        self.head = head


        
    
        
    




      
    



