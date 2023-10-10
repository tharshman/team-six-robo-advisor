from validators import NameValidator, AgeValidator, AgeOfRetirementValidator, AbstractValidator,\
                        SexAtBirthValidator, ValidatorType


class ValidatorFactory:
    @staticmethod
    def get_validator(validator_type: ValidatorType) -> AbstractValidator:
        match validator_type:
            case ValidatorType.NAME:
                return NameValidator()
            case ValidatorType.AGE:
                return AgeValidator()
            case ValidatorType.SEX_AT_BIRTH:
                return SexAtBirthValidator()
            case ValidatorType.AGE_OF_RETIREMENT:
                return AgeOfRetirementValidator()
            case _:
                raise ValueError("Invalid Validator Type")
