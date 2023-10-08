from models import AssetAllocationTable, UserInfo


class AssetAllocationStrategizer:
    def __init__(self, user_info: UserInfo):
        self._user_info = user_info

    def calculate_for_user(self) -> AssetAllocationTable:
        pass
