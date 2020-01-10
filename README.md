# Syntax dashboard

Projet fait dans le cadre du cours **Langages de script**
Il s'agit d'une interface graphique donnant quelques statistiques simples sur un fichier conllu.
Elles permet également de générer une table de relations entre dépendances.
Elle possède également un éditeur très basique pour modifier un ou plusieurs élements d'une phrase.
L'intéret est de pouvoir envoyer les phrases selectionnées dans la table de relation directement dans l'éditeur. Ceci afin de faciliter la correction des potentielles erreurs détectées. 

### Requirements

```
pip3 install -r requirements.txt
```

### Run

```
python3 run.py
```

# Guide d'utilisation

## 1. Importer un fichier

Le système prend en charge un fichier au format **CoNNL** *parfaitement formé*.

Ex:

![](https://s5.gifyu.com/images/ezgif.com-video-to-gif9b6c72424b5a27fe.gif)

## 2. Choissir la taille du corpus

L'utilisateur peut changer la taille du corpus
*Attention! A chaque modification, tous les calculs sont réeffectués*.

Ex:

On peut selectionner 50% du corpus ou seulement sont troisème quart : de 50% à 75%.

![](https://s5.gifyu.com/images/taille_corpus.gif)

## 3. Visualiser les statistiques

Après l'upload du fichier, des statistiques simples sur les **POS Tag** et **Dependances** sont calculés automatiquement.

![](https://s5.gifyu.com/images/graph1e4342c25077602e.gif)


## 4. Génerer la table des relations

Vous pouvez générer une table des relations très facilement grâce au bouton *Generate relation table* .

Ex : 

![](https://s5.gifyu.com/images/generate_tableau.gif)

## 5. Visualisation des phrases obtenues par la table des relations

Pour afficher les phrases contenant une relation, il vous suffit simplement de cliquer sur une des cellules du tableau.

Ex : 

![](https://s5.gifyu.com/images/phrase5a7b91428611aa7e.gif)

## 5. Modifier les arbres

La partie "**Quick edit tree**" contient une liste déroulante des phrases contennues dans le fichier importé.
Choississez une de ces phrases pour observer et modifier ses noeuds.
Vous pouvez également envoyer n'importe quelle phrase obtenue par la table de relation dans l'éditeur en cliquant dessus.

Utilisation de l'éditeur :
* Modifier le contenu d'une cellule : Selectionner la celluler sur la cellule et modifier son contenu
* Réinitialiser un arbre : cliquer sur "**Reset**"
* Ajouter un noeud : Entrez l'index du node puis cliquez sur "**Ade node**"
* Enregistrer les modifications : Cliquer sur "**Save tree**"
*Attention : N'oubliez pas d'enregistrer vos midifications avant de changer d'arbre ou d'exporter les résultats*

Ex : 

![](https://s5.gifyu.com/images/quick_edit.gif)

## 6. Exporter et télécharger un nouveau fichier CoNNL avec les modification

Allez dans la partie "**Export a new conll file**", entrez le nom de fichier souhaité puis cliquer sur exporter.
Vous pouvez télécharger en cliquant sur lien généré.

## Contact

```
- Pierre Rochet / pierre-rochet@outlook.fr
- Alican Yüksel / alicanyuksel@outlook.com
```
