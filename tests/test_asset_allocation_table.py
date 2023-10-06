from models.asset_allocation_table import AssetAllocationTable
from unittest import TestCase


class TestAssetAllocationTable(TestCase):
    def test_add_allocation(self):
        table = AssetAllocationTable()
        table.add_allocation(10, 50, 50)
        self.assertEqual(table.get_allocation_count(), 1)

    def test_get_allocation_count(self):
        table = AssetAllocationTable()
        self.assertEqual(table.get_allocation_count(), 0)

    def test_render_table(self):
        table = AssetAllocationTable()
        self.assertEqual(table.render_table(), "")
