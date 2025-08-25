

COMMENT DEPLOYER DIRECTEMENT A PARTIR DDE RIEN DU TOUT JUSTE LES FICHIERS EN LOCAL DANS UN DOCKER SAN PYTHON NI RIEN 
PREREQUIS "CLIENT" DOCKER : INSTALLER APP DOCK FOR WINDOWS PAS BESOIN DE COMPTE

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `.\env\Scripts\Activate.ps1`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer et faire des tests via admin pour alimenter la base de données.

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `.\env\Scripts\Activate.ps1`
- `flake8`

#### Tests unitaires (et enregistrement d'un rapport en txt)

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest > rapport.txt` 

#### Base de données

Vérifier que tout est ok en lançant 
`python check_sql_database.py`
puis en allant voir le contenu du rapport créé : rapport_sql.txt

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `difficile`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\env\Scripts\Activate.ps1` 


Installation avec Docker
------------------------

1. **Construisez l'image Docker** :

   .. code-block:: bash

      docker build -t nom-de-l-image .

2. **Lancez le conteneur** :

   .. code-block:: bash

      docker run -d -p 8000:8000 nom-de-l-image

3. **Accédez au projet** :

   Ouvrez un navigateur et allez à l’adresse suivante :

   .. code-block:: none

      http://localhost:8000
