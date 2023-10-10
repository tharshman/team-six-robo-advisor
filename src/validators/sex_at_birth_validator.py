from validators import AbstractValidator


class SexAtBirthValidator(AbstractValidator):
    def validate(self, value: str, second_value=None) -> (bool, str):
        clean_value = value.strip().lower()

        if len(clean_value) == 0:
            return False, "Sex is empty"

        if clean_value == "m" \
                or clean_value == "male" \
                or clean_value == "f" \
                or clean_value == "female":
            return True, None

        return False, "Invalid value for sex"
