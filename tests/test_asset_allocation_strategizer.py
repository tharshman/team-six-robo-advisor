# Import standard libraries
from unittest import TestCase

# Import local modules
from models import UserInfo, SexAtBirth
from services import AssetAllocationStrategizer


class TestAssetAllocationStrategizer(TestCase):
    def test_with_even_ages(self):
        user = UserInfo("Vin", 50, SexAtBirth.MALE, 70, 78)
        sut = AssetAllocationStrategizer(user)
        table = sut.calculate_for_user()
        self.assertEqual(8, table.get_allocation_count())

    def test_with_odd_ages(self):
        user = UserInfo("Vin", 54, SexAtBirth.MALE, 73, 78)
        sut = AssetAllocationStrategizer(user)
        table = sut.calculate_for_user()
        self.assertEqual(7, table.get_allocation_count())
