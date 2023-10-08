from models import UserInfo


class LifeExpectancyCalculator:
    def __init__(self):
        self._expectancy = int()

    def add_expectancies(self, age, sex, age_of_retirement):
        expectancies = UserInfo(age, sex, age_of_retirement)
        self._expectancy.append(expectancies)
