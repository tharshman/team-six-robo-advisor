from unittest import TestCase

from models import UserInfo, SexAtBirth

class TestUserInfo(TestCase):
    def test_expected_age_of_death(self):
        user = UserInfo("Vin", 49, SexAtBirth.MALE, 70, 29)
        self.assertEqual(user.expected_age_of_death, 78)
