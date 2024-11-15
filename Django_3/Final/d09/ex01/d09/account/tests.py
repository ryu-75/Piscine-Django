from django.test import TestCase, Client
from account.models import User
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterTestCase(TestCase):
    def test_register_success(self):
        """
        Test to register a user and verify if exist in database
        """
        print("---- Register a user ----")
        client = Client()
        response = client.post('/register/', {
            'username': 'test',
            'password': '1234',
            'repeat_password': '1234',
            'image': ''
        })
        if response.status_code != 200:
            print("Register failed ❌")
        self.assertEqual(response.status_code, 200)
        print("Register success ✅")
        self.assertTrue(User.objects.filter(username='test').exists())
        print("User exist in database ✅")