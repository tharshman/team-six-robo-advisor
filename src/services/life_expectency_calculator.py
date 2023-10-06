from models.user_info import UserInfo

class LifeExpectencyCalculator:
    def __init__(self):
        self._expectency = int()

    def add_expectencies(self, age, sex, age_of_retirement):
        expectencies = UserInfo(age, sex, age_of_retirement)
        self._expectency.append(expectencies)
        
