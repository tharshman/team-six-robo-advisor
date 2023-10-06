
from models.user_info import AssetAllocation

class LifeExpectencyCalculator:
    def __init__(self, age, sex, life_exp):
        self._age = age
        self._sex = sex
        self._life_exp = life_exp
