# Import standard libraries
from unittest import TestCase

# Import local modules
from models import UserInfo, SexAtBirth
from services import AssetAllocationStrategizer


class TestAssetAllocationStrategizer(TestCase):
    def test_with_valid_ages(self):
        user = UserInfo("Vin", 49, SexAtBirth.MALE, 73, 29)
        sut = AssetAllocationStrategizer(user)
        table = sut.calculate_for_user()
        self.assertEqual(6, len(table))

