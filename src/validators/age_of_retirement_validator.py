from validators import AbstractValidator


class AgeOfRetirementValidator(AbstractValidator):
    def __init__(self, age_of_retirement: str, current_age: int):
        self._age_of_retirement = age_of_retirement
        self._current_age = current_age

    def validate(self) -> (bool, str):
        if len(self._age_of_retirement.strip()) == 0:
            return False, "Age of retirement is empty"

        try:
            real_age_of_retirement = int(self._age_of_retirement)
        except ValueError:
            return False, "Age of retirement should be a whole number"

        if real_age_of_retirement <= self._current_age:
            return False, "The retirement age needs to be in the future"

        return True, None
