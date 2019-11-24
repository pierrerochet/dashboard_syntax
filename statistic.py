import database
import numpy as np


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

    pos_stats, dep_stats = array_data(database_sized, pos_tag, dep_tag)
    pos_tag_list = database.pos_tag_extraction(pos_tag)
    diversity_token = len(set(seq_token))
    total_token = sum(seq_num_token)

    mean_token = np.mean(np.array(seq_num_token))
    std_token = np.std(np.array(seq_num_token))
    std_token = "{:.2f}".format(std_token)

    g_stats = {"total": total_token, "diversity": diversity_token, "mean": mean_token, "std": std_token,
               "sentence": total_sentence}

    return g_stats, pos_stats, dep_stats, pos_tag_list


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


def moyenne(pos_tag_choisi, data_pos_tag):
    try:
        resultat = f"Moyenne de {pos_tag_choisi} : {np.mean(np.array(data_pos_tag[pos_tag_choisi]))}"
        return resultat

    except KeyError:
        return "Choisir un POS tag"


def ecart_type(pos_tag_choisi, data_pos_tag):
    try:
        resultat = f"Ecart-type de {pos_tag_choisi} : {np.std(np.array(data_pos_tag[pos_tag_choisi]))}"
        return resultat
    except KeyError:
        return "Choisir un POS tag"
