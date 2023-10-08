from models import UserInfo


class LifeExpectancyCalculator:
    def __init__(self):
        self._expectancy = int()

    def add_expectancies(self, age, sex, age_of_retirement):
        expectancies = UserInfo(age, sex, age_of_retirement)
        self._expectancy.append(expectancies)

    def calculate_for_user(self, user_info: UserInfo) -> UserInfo:
        # TODO: perform calculation with actuary data, append it to user_info and return user_info object
        return user_info

    def __load_actuary_data(self):
        # TODO: load actuary data
        pass
