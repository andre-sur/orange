from django.test import TestCase, Client
from django.urls import reverse

class SiteIndexTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
