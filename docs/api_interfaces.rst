Interfaces de programmation
===========================

Le projet Orange County Lettings est une application Django, dont les fonctionnalités se font via des vues HTML plutôt que par une API REST complète. 
Cependant, les interfaces de programmation internes (vues, URL, modèles) constituent l'ossature du projet.

Vues (views)
------------

Les vues sont réparties dans plusieurs modules selon leur fonction :

- **oc_lettings_site.views**
  - `index` : Vue principale d’accueil du site.

- **lettings.views**
  - `index` : Affiche la liste des locations disponibles.
  - `letting` : Affiche les détails d’un logement spécifique.

- **profiles.views**
  - `index` : Liste tous les profils d’utilisateurs.
  - `profile` : Affiche les informations détaillées d’un utilisateur.

URLs (routes)
-------------

Les URL sont définies dans `urls.py` :

- `/` → Vue d’accueil
- `/lettings/` → Liste des locations
- `/lettings/<int:letting_id>/` → Détails d’une location
- `/profiles/` → Liste des profils
- `/profiles/<str:username>/` → Détail d’un profil utilisateur

Modèles accessibles
-------------------

Les modèles sont les suivants :

- `Letting`
- `Address`
- `Profile`


