class AgeValidator:
    @staticmethod
    def validate(value: str) -> (bool, str):
        if len(value.strip()) == 0:
            return False, "Age is empty"

        try:
            age = int(value)
        except ValueError:
            return False, "Value is not an integer"

        return True, None
