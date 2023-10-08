from validators import AbstractValidator


class AgeValidator(AbstractValidator):
    def __init__(self, value):
        self._value = value

    def validate(self) -> (bool, str):
        if len(self._value.strip()) == 0:
            return False, "Age is empty"

        try:
            age = int(self._value)
        except ValueError:
            return False, "Value is not an integer"

        return True, None
