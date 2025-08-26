
Déploiement local (développement)
---------------------------------

1. **Cloner le dépôt**

   .. code-block:: bash

      git clone https://github.com/votre-utilisateur/orange-county-lettings.git
      cd orange-county-lettings

2. **Créer un environnement virtuel**

   .. code-block:: bash

      python -m venv env
      source env/bin/activate  # sous Linux/macOS
      env\Scripts\activate     # sous Windows

3. **Installer les dépendances**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Lancer le serveur de développement**

   .. code-block:: bash

      python manage.py runserver


Déploiement en production avec Docker
-------------------------------------

1. **Construire l'image Docker**

   .. code-block:: bash

      docker build -t orange-county-lettings .

2. **Lancer un conteneur localement**

   .. code-block:: bash

      docker run -d -p 8000:8000 orange-county-lettings

   Le site sera accessible sur http://localhost:8000

3. **Déploiement sur Render (ou tout autre PaaS)**

   - Pousser l’image sur DockerHub si nécessaire :

     .. code-block:: bash

        docker tag orange-county-lettings andresur/orange-county-lettings
        docker push andresur/orange-county-lettings

   - Créer un service web sur [https://render.com](https://render.com)
   - Ajouter les variables d’environnement nécessaires (`DEBUG`, `ALLOWED_HOSTS`, etc.)
   - Renseigner le `Dockerfile` dans le dépôt.
   - Définir la commande de lancement (par exemple : `gunicorn oc_lettings_site.wsgi:application`)

Maintenance et mise à jour
--------------------------

- Pour appliquer des mises à jour, faire un `git push` vers la branche déployée.
- Render (ou un autre système CI/CD) relancera automatiquement le build.
- Pour tester avant en local :

  .. code-block:: bash

     docker-compose down
     docker-compose up --build

Sauvegarde de la base de données
--------------------------------

Si la base est en SQLite :

- Faire une copie du fichier `.sqlite3`

   .. code-block:: bash

      cp new_base.sqlite3 backup.sqlite3
