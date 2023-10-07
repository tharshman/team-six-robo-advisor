class AgeOfRetirementValidator:
    @staticmethod
    def validate(age_of_retirement: str, current_age: int) -> (bool, str):
        if len(age_of_retirement.strip()) == 0:
            return False, "Age of retirement is empty"

        try:
            real_age_of_retirement = int(age_of_retirement)
        except ValueError:
            return False, "Age of retirement should be a whole number"

        if real_age_of_retirement <= current_age:
            return False, "The retirement age needs to be in the future"

        return True, None
