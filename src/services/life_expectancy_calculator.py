# import system modules
import csv
import sys
from pathlib import Path

# Import local modules
from models import UserInfo, SexAtBirth


class LifeExpectancyCalculator:
    def __init__(self, user_info: UserInfo, actuary_data_file_path: str):
        self._user_info = user_info
        self._actuary_data_file_path = LifeExpectancyCalculator.__fetch_resource(Path(actuary_data_file_path))
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
        with open(self._actuary_data_file_path, "r") as file:
            reader = csv.DictReader(file)
            table = list(reader)
        return table

    @staticmethod
    def __fetch_resource(resource_path: Path) -> Path:
        try:  # running as *.exe; fetch resource from temp directory
            base_path = Path(sys._MEIPASS)
        except AttributeError:  # running as script; return unmodified path
            return resource_path
        else:  # return temp resource path
            return base_path.joinpath(resource_path)
