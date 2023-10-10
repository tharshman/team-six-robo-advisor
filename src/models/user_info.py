from models import SexAtBirth


class UserInfo:
    def __init__(self, name: str, age: int, sex: SexAtBirth, age_of_retirement: int, life_expectancy=0):
        self._name = name
        self._age = age
        self._sex_at_birth = sex
        self._age_of_retirement = age_of_retirement
        self._life_expectancy = life_expectancy

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def age_of_retirement(self):
        return self._age_of_retirement

    @age_of_retirement.setter
    def age_of_retirement(self, value):
        self._age_of_retirement = value

    @property
    def age_of_life_expectancy(self):
        return self._age_of_life_expectancy

    @age_of_life_expectancy.setter
    def age_of_life_expectancy(self, value):
        self._age_of_life_expectancy = value

    @property
    def sex_at_birth(self):
        return self._sex_at_birth

    @sex_at_birth.setter
    def sex_at_birth(self, value):
        self._sex_at_birth = value
