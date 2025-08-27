from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse complète pour une location.

    Attributs:
        number (PositiveIntegerField): Numéro de rue, maximum 9999.
        street (CharField): Nom de la rue (max 64 caractères).
        city (CharField): Nom de la ville (max 64 caractères).
        state (CharField): Code de l'état sur 2 caractères.
        zip_code (PositiveIntegerField): Code postal, maximum 99999.
        country_iso_code (CharField): Code pays ISO sur 3 caractères.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField
    (validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        db_table = "oc_lettings_site_address"
        managed = False
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def __str__(self):
        """
        Retourne une représentation lisible de l'adresse.

        Returns:
            str: Numéro et nom de la rue, ex: "123 Main Street".
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Représente une location.

    Attributs:
        title (CharField): Titre de la location (max 256 caractères).
        address (OneToOneField): L'adresse associée à cette location.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "oc_lettings_site_letting"
        managed = False

    def __str__(self):
        """
        Retourne une représentation lisible de la location.

        Returns:
            str: Le titre de la location.
        """
        return self.title
