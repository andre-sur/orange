import sqlite3

# Chemin vers ta base de données SQLite
db_path = "new_base.sqlite3"

# Fichier de sortie
output_file = "rapport_sql.txt"

# Se connecter à la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

with open(output_file, "w", encoding="utf-8") as f:
    # 1. Afficher toutes les tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    f.write("Tables de la base :\n")
    for table in tables:
        f.write(f"{table[0]}\n")
    f.write("\n")

    # 2. Afficher les colonnes de la table Profile
    cursor.execute("PRAGMA table_info(profiles_profile);")
    columns = cursor.fetchall()
    f.write("Colonnes de la table Profile :\n")
    for col in columns:
        f.write(f"{col[1]} ({col[2]})\n")
    f.write("\n")

    # 3. Lancer une requête pour favorite_city commençant par 'B'
    cursor.execute(
        "SELECT user_id, favorite_city FROM " \
        "profiles_profile WHERE favorite_city LIKE 'P%';"
    )
    rows = cursor.fetchall()
    f.write("Résultats des profils avec favorite_city commençant par P :\n")
    for row in rows:
        f.write(f"user_id: {row[0]}, favorite_city: {row[1]}\n")

# Fermer la connexion
conn.close()

print(f"Rapport écrit dans {output_file}")
