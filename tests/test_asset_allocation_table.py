from models import AssetAllocationTable
from unittest import TestCase


class TestAssetAllocationTable(TestCase):
    def test_add_allocation(self):
        table = AssetAllocationTable()
        table.add_allocation(10, 50, 50)
        self.assertEqual(table.get_allocation_count(), 1)

    def test_get_allocation_count(self):
        table = AssetAllocationTable()
        self.assertEqual(table.get_allocation_count(), 0)

    def test_convert_to_string(self):
        table = AssetAllocationTable()
        self.assertEqual(str(table), "test")
