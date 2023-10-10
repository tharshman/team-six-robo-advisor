from validators import AbstractValidator


class AgeValidator(AbstractValidator):
    def validate(self, value: str, second_value=None) -> (bool, str):
        if len(value.strip()) == 0:
            return False, "Age is empty"

        try:
            age = int(value)
        except ValueError:
            return False, "Value is not an integer"

        return True, None
