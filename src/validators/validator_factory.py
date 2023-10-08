from validators import NameValidator, AgeValidator, AgeOfRetirementValidator, AbstractValidator,\
                        SexAtBirthValidator, ValidatorType


class ValidatorFactory:
    @staticmethod
    def get_validator(validator_type: ValidatorType, value: str, second_value: any = None) -> AbstractValidator:
        match validator_type:
            case ValidatorType.NAME:
                return NameValidator(value)
            case ValidatorType.AGE:
                return AgeValidator(value)
            case ValidatorType.SEX_AT_BIRTH:
                return SexAtBirthValidator(value)
            case ValidatorType.AGE_OF_RETIREMENT:
                return AgeOfRetirementValidator(value, int(second_value))
            case _:
                raise ValueError()
