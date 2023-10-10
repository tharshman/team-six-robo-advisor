from models import AssetAllocationTable
from unittest import TestCase


class TestAssetAllocationTable(TestCase):
    def test_add_allocation(self):
        table = AssetAllocationTable()
        table.add_allocation(10, 50, 50)
        self.assertEqual(len(table), 1)

    def test_len(self):
        table = AssetAllocationTable()
        self.assertEqual(len(table), 0)

    def test_iteration(self):
        table = AssetAllocationTable()
        table.add_allocation(10, 50, 50)
        self.assertEqual(len(table), 1)
        for row in table:
            print(f"YTR: {row.years_to_retirement}   Stock: {row.percent_in_stock}   Bonds: {row.percent_in_bonds}")
