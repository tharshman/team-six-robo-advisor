import csv
from models import UserInfo, SexAtBirth


class LifeExpectancyCalculator:
    LIFE_EXPECTANCY_DATA_FILE = "life_expectancy_db.csv"

    def __init__(self, user_info: UserInfo):
        self._user_info = user_info
        self._actuary_table = self.__load_actuary_data()

    def calculate_for_user(self) -> UserInfo:
        for row in self._actuary_table:
            if int(row["Age"]) == self._user_info.age:
                if self._user_info.sex_at_birth == SexAtBirth.MALE:
                    self._user_info.life_expectancy = int(float(row["Male"]))
                elif self._user_info.sex_at_birth == SexAtBirth.FEMALE:
                    self._user_info.life_expectancy = int(float(row["Female"]))
                else:
                    raise ValueError(f"No data available for sex {self._user_info.sex_at_birth}")
                break

        if self._user_info.life_expectancy == 0:
            raise ValueError(f"No data available for age {self._user_info.age}")

        return self._user_info

    def __load_actuary_data(self) -> list:
        with open(self.LIFE_EXPECTANCY_DATA_FILE, "r") as file:
            reader = csv.DictReader(file)
            table = list(reader)
        return table
