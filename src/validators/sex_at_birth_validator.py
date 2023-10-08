from validators import AbstractValidator


class SexAtBirthValidator(AbstractValidator):
    def __init__(self, value):
        self._value = value

    def validate(self) -> (bool, str):
        clean_value = self._value.strip().lower()

        if len(clean_value) == 0:
            return False, "Sex is empty"

        if clean_value == "m" \
                or clean_value == "male" \
                or clean_value == "f" \
                or clean_value == "female":
            return True, None

        return False, "Invalid value for sex"
