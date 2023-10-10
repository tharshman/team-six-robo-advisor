from validators import AbstractValidator


class NameValidator(AbstractValidator):
    def validate(self, value: str, second_value=None) -> (bool, str):
        trimmed_name = value.strip()

        if len(trimmed_name) == 0:
            return False, "Name is empty"

        if len(trimmed_name) >= 100:
            return False, "Name is too long"

        return True, None
