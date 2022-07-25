from unicodedata import name
from django.test import Client,TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="test123"
        )
        self.client.force_login(self.admin_user)

        self.user=get_user_model().objects.create_user(
            email="Test@example.com",
            password="testadmin123",
            name="Test User"
        )

    def test_user_list(self):
        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res,self.user.email)
        self.assertContains(res,self.user.name)



