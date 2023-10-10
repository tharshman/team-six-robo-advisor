from models import AssetAllocation


class AssetAllocationTable:
    def __init__(self):
        self._allocations = list()
        self._index = 0

    def add_allocation(self, years_to_retirement, percent_in_stock, percent_in_bonds):
        allocation = AssetAllocation(years_to_retirement, percent_in_stock, percent_in_bonds)
        self._allocations.append(allocation)

    def __len__(self):
        return len(self._allocations)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._allocations):
            result = self._allocations[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
