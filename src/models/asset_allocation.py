class AssetAllocation:
    def __init__(self, years_to_retirement, percent_in_stock, percent_in_bonds):
        self._years_to_retirement = years_to_retirement
        self._percent_in_stock = percent_in_stock
        self._percent_in_bonds = percent_in_bonds

    @property
    def years_to_retirement(self):
        return self._years_to_retirement

    @years_to_retirement.setter
    def years_to_retirement(self, value):
        self._years_to_retirement = value

    @property
    def percent_in_stock(self):
        return self._percent_in_stock

    @percent_in_stock.setter
    def percent_in_stock(self, value):
        self._percent_in_stock = value

    @property
    def percent_in_bonds(self):
        return self._percent_in_bonds

    @percent_in_bonds.setter
    def percent_in_bonds(self, value):
        self._percent_in_bonds = value
