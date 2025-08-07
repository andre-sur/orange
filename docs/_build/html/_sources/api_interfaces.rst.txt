Interfaces de programmation
===========================

Le projet Orange County Lettings est une application Django de type monolithique, qui expose ses fonctionnalités via des vues HTML plutôt que par une API REST complète. Cependant, les interfaces de programmation internes (vues, URL, modèles) constituent l'ossature du projet.

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

Les URL sont définies dans les fichiers `urls.py` respectifs de chaque application :

- `/` → Vue d’accueil
- `/lettings/` → Liste des locations
- `/lettings/<int:letting_id>/` → Détails d’une location
- `/profiles/` → Liste des profils
- `/profiles/<str:username>/` → Détail d’un profil utilisateur

Modèles accessibles
-------------------

Les modèles peuvent être utilisés dans des scripts internes, des tâches d’administration ou dans des appels depuis d’autres composants Django :

- `Letting`
- `Address`
- `Profile`

Exemple d’utilisation interne
-----------------------------

Voici un exemple d’appel interne depuis une autre vue Django :

```python
from lettings.models import Letting

def nombre_de_locations():
    return Letting.objects.count()
