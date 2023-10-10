from validators import AbstractValidator


class AgeOfRetirementValidator(AbstractValidator):
    def validate(self, value: str, second_value) -> (bool, str):
        age_of_retirement = value.strip()

        if len(age_of_retirement) == 0:
            return False, "Age of retirement is empty"

        try:
            current_age = int(second_value)
        except ValueError:
            return False, "Your current age should be a whole number"

        try:
            real_age_of_retirement = int(age_of_retirement)
        except ValueError:
            return False, "Age of retirement should be a whole number"

        if real_age_of_retirement < 21 or real_age_of_retirement > 100:
            return False, "Age of retirement range needs to be between 21 and 100"

        if real_age_of_retirement <= current_age:
            return False, "The retirement age needs to be in the future"

        return True, None
