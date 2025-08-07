Guide de démarrage rapide
=========================

Ce guide vous permet de lancer rapidement le projet en environnement de développement.

Étapes de démarrage rapide
--------------------------

1. **Cloner le dépôt**

   .. code-block:: bash

      git clone https://github.com/votre-utilisateur/nom-du-projet.git
      cd nom-du-projet

2. **Créer un environnement virtuel**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate   # Linux/Mac
      .\venv\Scripts\activate    # Windows

3. **Installer les dépendances**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Lancer les migrations**

   .. code-block:: bash

      python manage.py migrate

5. **Démarrer le serveur de développement**

   .. code-block:: bash

      python manage.py runserver

6. **Accéder à l’application**

   Ouvrez votre navigateur et allez à l’adresse suivante :

   .. code-block:: none

      http://127.0.0.1:8000

Utilisation rapide avec Docker
------------------------------

1. **Construire et lancer le conteneur**

   .. code-block:: bash

      docker build -t nom-de-l-image .
      docker run -d -p 8000:8000 nom-de-l-image

2. **Accéder à l'application**

   Rendez-vous sur :

   .. code-block:: none

      http://localhost:8000

