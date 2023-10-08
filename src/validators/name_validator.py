from validators import AbstractValidator


class NameValidator(AbstractValidator):
    def __init__(self, value):
        self._value = value

    def validate(self) -> (bool, str):
        trimmed_name = self._value.strip()

        if len(trimmed_name) == 0:
            return False, "Name is empty"

        if len(trimmed_name) >= 100:
            return False, "Name is too long"

        return True, None
