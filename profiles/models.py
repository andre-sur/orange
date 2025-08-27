from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profil étendu d'un utilisateur.

    Attributs:
        user (OneToOneField): L'utilisateur associé à ce profil.
        favorite_city (CharField): La ville
        favorite de l'utilisateur (optionnelle).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = "oc_lettings_site_profile"
        managed = False

    def __str__(self):
        """
        Retourne une représentation lisible du profil.

        Returns:
            str: Le nom d'utilisateur associé au profil.
        """
        return self.user.username
