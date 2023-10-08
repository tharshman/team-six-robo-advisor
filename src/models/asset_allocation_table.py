from models.asset_allocation import AssetAllocation


class AssetAllocationTable:
    def __init__(self):
        self._allocations = list()

    def add_allocation(self, years_to_retirement, percent_in_stock, percent_in_bonds):
        allocation = AssetAllocation(years_to_retirement, percent_in_stock, percent_in_bonds)
        self._allocations.append(allocation)

    def get_allocation_count(self):
        return len(self._allocations)

    def __str__(self):
        return "test"
