from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


class ProfilesTests(TestCase):
    """
    TestCase pour les vues de l'application 'profiles'.

    Cette classe vérifie que :
    - La page d'index des profils est accessible.
    - La page de détail d'un profil spécifique est accessible.

    Attributs:
        client (Client): Client de test pour simuler les requêtes HTTP.
        user (User): Utilisateur créé pour les tests.
        profile (Profile): Profil associé à l'utilisateur pour les tests.
    """

    def setUp(self):
        """
        Initialise les objets nécessaires pour les tests.

        - Crée un client de test.
        - Crée un utilisateur fictif.
        - Crée un profil associé à cet utilisateur.
        """
        self.client = Client()
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Lyon"
        )

    def test_profiles_index(self):
        """
        Teste que la vue de la liste des profils retourne un code HTTP 200.
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)

    def test_profile_detail(self):
        """
        Teste que la vue du détail d'un profil spécifique
          retourne un code HTTP 200.
        """
        response = self.client.get(
            reverse("profile", args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)

