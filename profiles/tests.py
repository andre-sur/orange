from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


class ProfilesTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Lyon")

    def test_profiles_index(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)

    def test_profile_detail(self):
        response = self.client.get(
            reverse("profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
