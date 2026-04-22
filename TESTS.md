# Plan de Tests - fsociety

## Description

Ce document recense les cas de tests critiques pour le projet **fsociety**, un framework de tests d'intrusion en Python. Les tests couvrent les fonctionnalités principales selon un découpage descendant (fonctionnel → module → cas).

Les tests marqués **[NR]** sont des **tests de non-régression** liés aux anomalies corrigées lors de l'Atelier 2.

---

## Tableau des cas de tests

| # | Fonctionnalité | Module | Type | Scénario | Résultat Attendu | Non-Régression |
|---|---|---|---|---|---|---|
| T01 | Lecture de configuration | `core/config.py` | Cas usuel | Lire une configuration existante et valide | Retourne un objet `RawConfigParser` avec toutes les clés par défaut | |
| T02 | Création de configuration | `core/config.py` | Cas extrême | Appeler `get_config()` quand le répertoire `INSTALL_DIR` n'existe pas | Le répertoire et le fichier de config sont créés automatiquement | |
| T03 | Clé manquante en config | `core/config.py` | Cas d'erreur | Fichier de config présent mais avec une clé manquante | `check_config()` ajoute la valeur par défaut sans erreur | **[NR]** |
| T04 | Écriture de configuration | `core/config.py` | Cas usuel | Modifier une valeur puis appeler `write_config()` | La valeur modifiée est persistée dans le fichier | |
| T05 | Ajout d'un hôte valide | `core/hosts.py` | Cas usuel | Appeler `add_host("example.com")` | L'hôte apparaît dans la liste retournée par `get_hosts()` | |
| T06 | Ajout d'un hôte vide | `core/hosts.py` | Cas d'erreur | Appeler `add_host("")` | Lève une `ValueError` | **[NR]** |
| T07 | Liste hôtes - fichier absent | `core/hosts.py` | Cas extrême | Appeler `get_hosts()` quand `hosts.txt` n'existe pas | Retourne une liste vide `[]` sans exception | **[NR]** |
| T08 | Ajout d'un username valide | `core/usernames.py` | Cas usuel | Appeler `add_username("admin")` | L'username apparaît dans la liste retournée par `get_usernames()` | |
| T09 | Liste usernames - fichier absent | `core/usernames.py` | Cas extrême | Appeler `get_usernames()` quand `usernames.txt` n'existe pas | Retourne une liste vide `[]` sans exception | **[NR]** |
| T10 | Décodage base64 valide | `core/utilities.py` | Cas usuel | Décoder la chaîne `"aGVsbG8="` | Retourne `b"hello"` correctement | |
| T11 | Décodage base64 avec padding | `core/utilities.py` | Cas extrême | Décoder une chaîne base64 sans padding explicite | Décode correctement sans exception | |
| T12 | Décodage base64 invalide | `core/utilities.py` | Cas d'erreur | Décoder une chaîne non-base64 (`"!!invalid!!"`) | Lève une `binascii.Error` | |
| T13 | Nom de module | `core/menu.py` | Cas usuel | Appeler `module_name()` sur un module Python | Retourne le dernier segment du nom du module | |
| T14 | Format du prompt | `core/menu.py` | Cas usuel | Appeler `prompt()` sans argument | Retourne `"\nfsociety ~/# "` | |
| T15 | Format du prompt avec chemin | `core/menu.py` | Cas usuel | Appeler `prompt("information_gathering")` | Contient `"information_gathering"` dans la chaîne retournée | |
| T16 | Outil installé | `core/repo.py` | Cas usuel | Appeler `installed()` sur un `GitHubRepo` dont le chemin existe | Retourne `True` | |
| T17 | Outil non installé | `core/repo.py` | Cas usuel | Appeler `installed()` sur un `GitHubRepo` dont le chemin n'existe pas | Retourne `False` | |
| T18 | Représentation str du repo | `core/repo.py` | Cas usuel | Appeler `str()` sur un `GitHubRepo("owner/My-Tool")` | Retourne `"my_tool"` (minuscules, tirets remplacés par `_`) | |
| T19 | Dépendances pip - liste | `core/repo.py` | Cas usuel | Appeler `print_pip_deps(["requests", "rich"])` | Affiche un tableau sans exception | |
| T20 | Dépendances pip - valeur invalide | `core/repo.py` | Cas d'erreur | Appeler `print_pip_deps(42)` (type invalide) | Lève une `ValueError` | **[NR]** |
| T21 | Commande invalide dans le menu | `__main__.py` | Cas d'erreur | Entrer une commande non reconnue dans le menu principal | Affiche `"Invalid Command"` sans crash | |
| T22 | Commande vide dans le menu | `__main__.py` | Cas extrême | Appuyer sur Entrée sans commande | Affiche `"Invalid Command"` sans crash | |
| T23 | Accord utilisateur déjà accepté | `__main__.py` | Cas usuel | `agreement=true` dans la config | La fonction `agreement()` se termine immédiatement sans afficher les CGU | |
| T24 | Autocomplétion - texte partiel | `core/menu.py` | Cas usuel | `CommandCompleter.complete("inf", 0)` avec options correspondantes | Retourne la première option commençant par `"inf"` | |
| T25 | Autocomplétion - aucun résultat | `core/menu.py` | Cas extrême | `CommandCompleter.complete("xyz", 0)` sans option correspondante | Retourne `None` | |

---

## Résumé

| Type | Nombre |
|---|---|
| Cas usuel | 15 |
| Cas extrême | 5 |
| Cas d'erreur | 5 |
| **Total** | **25** |
| Tests de non-régression [NR] | 6 |

---

## Tests de non-régression (Atelier 2)

Les tests suivants correspondent aux anomalies identifiées et corrigées lors de l'Atelier 2 :

| ID | Anomalie couverte |
|---|---|
| T03 | Clé absente dans le fichier de configuration → crash au démarrage |
| T06 | Hôte vide accepté sans validation → écriture d'une ligne vide dans `hosts.txt` |
| T07 | Exception non gérée quand `hosts.txt` est absent |
| T09 | Exception non gérée quand `usernames.txt` est absent |
| T20 | Type invalide passé à `print_pip_deps()` ne lève pas d'erreur explicite |
