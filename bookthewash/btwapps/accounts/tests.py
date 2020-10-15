from django.test import TestCase

from btwapps.accounts.models.User import User
# Create your tests here.
class UserProfileTest(TestCase):
    def test(self):
        user = User(
            email="test@gmail.com",
            username="test_user",
            password="abc123"
        )

        user.save()

        self.assertTrue(
            hasattr(user,'profile')
        )
