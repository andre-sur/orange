Structure de la base de données et des modèles
==============================================

Le projet est basé sur une base de données relationnelle (SQLite en développement, potentiellement PostgreSQL en production).

Modèle : Letting
----------------

Le modèle **Letting** représente une location. Il est défini dans l'application `lettings`.

**Champs :**

- `title` : Titre de l'annonce.
- `address` (clé étrangère) : Référence à l'adresse liée à ce letting.

Modèle : Address
----------------

Le modèle **Address** est utilisé pour stocker les informations de localisation d’un Letting.

**Champs :**

- `number` : Numéro de rue.
- `street` : Rue.
- `city` : Ville.
- `state` : État ou province.
- `zip_code` : Code postal.
- `country_iso_code` : Code ISO du pays.

Modèle : Profile
----------------

Le modèle **Profile** étend l'utilisateur Django par défaut avec des informations supplémentaires. Il est défini dans l'application `profiles`.

**Champs :**

- `user` : Clé étrangère vers le modèle `User` de Django.
- `favorite_city` : Ville préférée de l'utilisateur.

Relations entre les modèles
---------------------------

- Un **Letting** est associé à une **Address** (relation 1-1).
- Un **Profile** est lié à un **User** standard de Django (relation 1-1).

Diagramme conceptuel (optionnel)
--------------------------------

.. note::

   Un diagramme de la base de données peut être généré avec des outils comme Django Extensions (`graph_models`) ou DBML pour aider à visualiser les relations.

