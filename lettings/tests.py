from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting


class LettingsTests(TestCase):

    def setUp(self):
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

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)

    def test_letting_detail(self):
        response = self.client.get(reverse("letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
