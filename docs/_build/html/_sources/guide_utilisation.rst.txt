Guide d’utilisation
===================

Ce guide décrit comment utiliser l’application Orange County Lettings du point de vue d’un utilisateur final. Il présente les principales fonctionnalités accessibles via l’interface web, avec des cas d’usage concrets.

Accès à l'application
---------------------

L'application est accessible via l’URL suivante (exemple de déploiement) :

    https://orange-vpow.onrender.com/

Navigation générale
-------------------

La page d’accueil propose deux sections principales :

- **Lettings** : Locations disponibles
- **Profiles** : Profils des utilisateurs

L’utilisateur peut naviguer via le menu de navigation situé dans la barre supérieure.

Cas d’utilisation
-----------------

### 1. Consulter la liste des locations

- Depuis la page d’accueil, cliquer sur **“Lettings”**.
- Une liste des logements disponibles s’affiche.
- Chaque entrée comporte un lien vers une page de détail.

### 2. Consulter les détails d’un logement

- Depuis la liste des locations, cliquer sur une location.
- Les informations suivantes sont affichées :
  - Titre
  - Adresse complète
  - Code postal, ville, état
  - Pays

### 3. Consulter les profils utilisateurs

- Cliquer sur **“Profiles”** depuis le menu.
- Une liste de tous les utilisateurs enregistrés s’affiche.

### 4. Voir le détail d’un profil

- Cliquer sur un nom d’utilisateur.
- La page affiche :
  - Nom d’utilisateur
  - Ville préférée

Public cible
------------

L’application est conçue pour :
- Les agents immobiliers souhaitant accéder à des données de location.
- Les administrateurs système via Django admin.
- Les utilisateurs voulant consulter des logements.

Limitations
-----------

- L’application ne permet pas encore la création/modification via interface publique.
- Pas de système d’authentification ou de gestion de session utilisateur (hors admin).

