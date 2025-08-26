Installation du projet
======================

Prérequis
---------

Avant d’installer le projet, assurez-vous d’avoir les éléments suivants :

- Python 3.8 ou version ultérieure
- pip
- virtualenv (recommandé pour installer de façon localisé)
- Git (si vous clonez depuis un dépôt)
- Docker 

Installation en local

1. **Clonez le dépôt** (si nécessaire) :

   .. code-block:: bash

      git clone https://github.com/andre-sur/orange.git
      cd nom-du-projet

2. **Créez et activez un environnement virtuel** :

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate   # Linux/Mac
      .\venv\Scripts\activate    # Windows

3. **Installez les dépendances** :

   .. code-block:: bash

      pip install -r requirements.txt

4. **Lancez le serveur de développement** :

   .. code-block:: bash

      python manage.py runserver

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

