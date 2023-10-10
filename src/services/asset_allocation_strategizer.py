from models import AssetAllocationTable, UserInfo


class AssetAllocationStrategizer:
    def __init__(self, user_info: UserInfo):
        self._user_info = user_info

    def calculate_for_user(self) -> AssetAllocationTable:
        # Calculate 5 year increments
        left_bound = self.__get_left_bound()
        right_bound = self.__get_right_bound()

        # Use Bogle Asset Allocation formula
        table = AssetAllocationTable()
        for i in range(left_bound, right_bound + 1, 5):
            bond_allocation = min(100, i)
            table.add_allocation(i - self._user_info.age_of_retirement, 100-bond_allocation, bond_allocation)

        return table

    def __get_left_bound(self):
        x = self._user_info.age_of_retirement

        # Work backwards until we're close to current age
        while x >= self._user_info.age:
            x -= 5

        # Go back one step if we passed age
        if x < self._user_info.age:
            x += 5
        return x

    def __get_right_bound(self):
        x = self._user_info.age_of_retirement

        # Work backwards until we're close to expected age of death
        while x <= self._user_info.expected_age_of_death:
            x += 5

        # Go back one step if we passed age
        if x > self._user_info.expected_age_of_death:
            x -= 5
        return x
