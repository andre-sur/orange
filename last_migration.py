# check_migration.py
import os
import django

# 1️⃣ Configurer le projet Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")  # <- Remplace myproject par ton projet
django.setup()

# 2️⃣ Importer la connexion DB
from django.db import connection

# 3️⃣ Définir l'app et la migration à vérifier
app_name = "oc_lettings_site"          # Nom de l'app tel qu'il est dans INSTALLED_APPS
migration_name = "0001_initial" # Nom de la migration

# 4️⃣ Interroger la table django_migrations
with connection.cursor() as cursor:
    cursor.execute(
        "SELECT app, name, applied FROM django_migrations WHERE app=%s AND name=%s",
        [app_name, migration_name]
    )
    row = cursor.fetchone()

# 5️⃣ Afficher le résultat
if row:
    print(f"La migration {row[1]} de l'app {row[0]} a été appliquée le : {row[2]}")
else:
    print(f"La migration {migration_name} de l'app {app_name} n'a jamais été appliquée.")
