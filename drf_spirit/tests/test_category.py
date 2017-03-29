from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from drf_spirit.models import Category


class CategoryTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'testadmin'
        self.email = 'testadmin@testing.com'
        self.password = 'testpass'
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.client.login(username=self.username, password=self.password)

    def test_get(self):
        resp = self.client.get(reverse('drf_spirit:category-list'))
        self.assertEqual(resp.status_code, 200)
