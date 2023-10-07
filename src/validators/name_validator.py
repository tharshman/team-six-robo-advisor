class NameValidator:
    @staticmethod
    def validate(value: str) -> (bool, str):
        if len(value.strip()) == 0:
            return False, "Name is empty"

        if len(value.strip()) >= 100:
            return False, "Name is too long"

        return True, None
