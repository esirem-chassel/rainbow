# rainbow

Ce projet est un générateur de rainbow tables,
à seule fin pédagogique, dans le cadre du module
"Soutien Informatique" en 3A FISA.

Il repose sur une stack Django + SQLite.

## Installation

> [!Note]
> Vous devriez envisager d'installer l'outil via un environnement virtuel.

Une fois le dépôt cloné, lancez un `pip install -r requirements.txt` pour lancer l'installation des prérequis nécessaires.

## Configuration



## Utilisation

### Rechercher un hash

Dans l'interface graphique, vous pouvez rechercher un hash.
La liste des sources correspondantes s'affichera.

### Générer un hash

Vous pouvez générer un hash en ligne de commande via `py manage.py generate`.

Par défaut, cela génère une source aléatoire d'une longueur aléatoire d'un maximum équivalent à la longueur maximale la plus petite autorisée dans la liste des flavors.

Cette commande prend deux arguments facultatifs:
- `--nb` : pour une génération aléatoire d'un nombre `nb` de chaînes sources
- `--src` : pour la génération des hashs pour une chaîne `src`

### Ajouter une flavor

Cela est possible dans l'interface graphique.

### Supprimer des hashs, supprimer des flavors

Cela est impossible par défaut, sauf en passant par l'interface administrateur.

## Annexes

### Django

La documentation de [Django](https://www.djangoproject.com/) est disponible sur le [site officiel de Django](https://docs.djangoproject.com/en/5.2/).

Une autre documentation est également [disponible sur le MDN (Mozilla Developer Network)](https://developer.mozilla.org/fr/docs/Learn_web_development/Extensions/Server-side/Django).

Ces documentations sont fournies pour votre culture et ne devraient pas,
à ce stade, être nécessaires, sauf cas particuliers.

### SQLite

La documentation de SQLite est disponible [sur le site officiel de SQLite](https://www.sqlite.org/docs.html).
