from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting


class LettingsTests(TestCase):
    """
    TestCase pour les vues de l'application 'lettings'.

    Cette classe vérifie :
    - L'accessibilité de la page d'index des lettings (test d'intégration).
    - L'accessibilité de la page de détail d'un letting spécifique (test d'intégration).

    Attributs:
        client (Client): Client de test pour simuler les requêtes HTTP.
        address (Address): Adresse utilisée pour créer un letting.
        letting (Letting): Objet Letting créé pour les tests.
    """

    def setUp(self):
        """
        Initialise les objets nécessaires pour les tests.

        - Crée un client de test.
        - Crée une adresse fictive.
        - Crée un letting associé à cette adresse.
        """
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street="Main Street",
            city="Paris",
            state="IDF",
            zip_code=75000,
            country_iso_code="FR",
        )
        self.letting = Letting.objects.create(
            title="Nice Letting", address=self.address
        )

    # ----------------------------
    # Test d'intégration
    # ----------------------------
    def test_lettings_index(self):
        """
        Vérifie que la vue de la liste des lettings retourne un code HTTP 200.

        Type: Test d'intégration
        Pourquoi: teste l'interaction entre la vue, le modèle et le template.
        """
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)

    # ----------------------------
    # Test d'intégration
    # ----------------------------
    def test_letting_detail(self):
        """
        Vérifie que la vue du détail d'un letting spécifique retourne un code HTTP 200.

        Type: Test d'intégration
        Pourquoi: teste l'interaction entre la vue, le modèle et le template.
        """
        response = self.client.get(reverse("letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)

    # ----------------------------
    # Exemple de test unitaire possible
    # ----------------------------
    def test_letting_str_method(self):
        """
        Vérifie la méthode __str__ du modèle Letting.

        Type: Test unitaire
        Pourquoi: teste uniquement la méthode __str__ sans interaction avec d'autres composants.
        """
        self.assertEqual(str(self.letting), "Nice Letting")
