Déploiement non local
=====================

Déploiement avec Docker
-----------------------

1. **Construire l’image Docker** :

   .. code-block:: bash

      docker build -t orange-county-lettings .

2. **Lancer un conteneur** :

   .. code-block:: bash

      docker run -d -p 8000:8000 orange-county-lettings

   Le site sera accessible sur :

   .. code-block:: none

      http://localhost:8000


Déploiement sur Render (ou autre PaaS)
--------------------------------------

1. **Pousser l’image Docker sur DockerHub (si nécessaire)** :

   .. code-block:: bash

      docker tag orange-county-lettings andresur/orange-county-lettings
      docker push andresur/orange-county-lettings

2. **Configurer un service web sur Render** :

   - Créer un service web sur `https://render.com <https://render.com>`_
   - Ajouter les variables d’environnement nécessaires (``DEBUG``, ``ALLOWED_HOSTS``, etc.)
   - Indiquer le ``Dockerfile`` présent dans le dépôt
   - Définir la commande de lancement, par exemple :

     .. code-block:: bash

        gunicorn oc_lettings_site.wsgi:application


Maintenance et mise à jour
--------------------------

- Pour appliquer des mises à jour, poussez vos changements :

  .. code-block:: bash

     git push

  Render (ou tout autre CI/CD configuré) déclenchera automatiquement un nouveau build.

- Pour tester les mises à jour en local avant déploiement :

  .. code-block:: bash

     docker-compose down
     docker-compose up --build


Sauvegarde de la base de données
--------------------------------

Si vous utilisez SQLite, il suffit de copier le fichier ``.sqlite3`` :

.. code-block:: bash

   cp new_base.sqlite3 backup.sqlite3
