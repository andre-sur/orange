# Utilise une image officielle Python 3.11 slim comme base
FROM python:3.11-slim

# Variables d’environnement pour Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crée et définit le dossier de travail dans le container
WORKDIR /app

# Installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie les fichiers requirements.txt dans le container
COPY requirements.txt /app/

# Met à jour pip et installe les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie tout le code source dans le container
COPY . /app/

# Expose le port 8000 pour le serveur Django
EXPOSE 8000

# lancer le serveur Django avec gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
# pour server DJango, utiliser
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
