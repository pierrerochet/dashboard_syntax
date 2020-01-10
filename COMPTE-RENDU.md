# Syntax Dashboard

### Objectif du projet

N'ayant pas de réelles compétences dans les interfaces graphiques nous voulions en réaliser une afin de se sentir plus à l'aise. Ayant en revanche l'habitude de travailler avec des fichiers CoNLL et connaissant le nombre répétitif de tâche que nous pouvons faire dessus nous avons décidé de créer un outil pour facilier leurs traitements. 
Nous avions plusieurs idée au départ : calculs statistiques, visualisation, parsing de texte, editeur, etc. 
Nous avons commencé par faire des calculs statistiques simples sur un corpus pour prendre les outils en mains puis nous avons dévié sur la génération d'une table de relation avec la possibilité de modifier, sauvegarder et télécharger les arbres. Ce qui a déjà représenté un grand travail.


### Les données (origine, format, statut juridique) et les traitements opérés sur celles-ci

Afin de tester notre système nous avons utilsés des fichiers conllu que nous possédions. En corpus test de référence nous proposons la partie test du corpus Sequoia téléchargable à cette adresse : 
(https://universaldependencies.org/), elle se trouve également dans le dossier data exemple_data. Les droits sont au format GPL.


### Méthodologie


La structure de base s'est faite à deux et relativement rapidement. Nous avons implémenté une grande partie de l'interface ensemble car nous devions et voulions chacun apprendre Dash : l'outil utilisé pour la réalisation de l'interface. 
Concernant les fonctionnalités, nous avons au départ travaillé chacun de notre coté en fonction de nos idées respectives. Nous avions au départ beaucoup d'idée ce qui laissait penser que nous pouvions réaliser de grandes choses. Malheureusement les nombreaux bugs que nous avons du corriger nous ont rapidement frainés. 80 % de notre temps de travail a été concacré au déboggage. Dès qu'un de nous deux a rencontré un problème il l'a partagé et ce problème à très souvent été résoulu par l'autre personne.


## Implémentations


Le projet est conçu par :

* [Dash](https://dash.plot.ly)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
* [Numpy](https://numpy.org/doc/)

Nous avons également ajouté un peu de css pour embellir le tout


## Résultat

Quelques mots sur ce qu'on a pu obtenir :

Malgré les nombreux bugs que nous avons du corrigé le système fonctionne dans son ensemble. Cependant nous n'avons pas eu le temps ni de faire beaucoup de test, ni d'optimiser. Un des plus gros défauts est le chargement de trop de fonctionnalité pour certaines actions. Nous avons reparti le code un maximum mais certaines fonctionnalités étant trop dépendantes d'autres nous n'avons pu trouver de meilleures solutions dans le temps imparti. Nous aurions donc aimé améliorer ce point qui est également très lié aux performances du système.
Concernant les fonctionnalités nous aurions également aimé proposé d'avantage de fonction mais nous avons préféré nous concentrer sur le bon fonctionnemnt des premières implémentations.
Ce que nous retenons de ce projet est qu'il n'est pas forcément difficile de réaliser le backend (python est agréable), ni le frontend(aujourd'hui beaucoup de méthode d'interface nous facilitent le travail), ce qui est particulièrement difficile est bien l'association des deux. Une fois que tout est lié, si une ligne dysfonctionne tout explose ! 
