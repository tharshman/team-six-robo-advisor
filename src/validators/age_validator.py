from validators import AbstractValidator


class AgeValidator(AbstractValidator):
    def validate(self, value: str, second_value=None) -> (bool, str):
        if len(value.strip()) == 0:
            return False, "Age is empty"

        try:
            age = int(value)
        except ValueError:
            return False, "Value is not an integer"

        if age < 21 or age > 100:
            return False, "Age range needs to be between 21 and 100"

        return True, None
