# Import local modules
from services import LifeExpectancyCalculator, AssetAllocationStrategizer
from validators import ValidatorFactory, ValidatorType
from models import UserInfo, SexAtBirth


def get_input(prompt: str, validator_type: ValidatorType, second_value: any = None) -> str:
    value_is_valid = False
    value = None
    validator = ValidatorFactory.get_validator(validator_type, second_value)
    while not value_is_valid:
        value = input(prompt)
        value_is_valid, error_message = validator.validate()
        if not value_is_valid:
            print(error_message)
            print("Let's try that again")
    return value


def get_user_info_from_inputs() -> UserInfo:
    name = get_input("Please enter your name:", ValidatorType.NAME)

    age = get_input("Please enter your age (only as a whole number):", ValidatorType.AGE)
    current_age = int(age)

    sex_at_birth = get_input("Please enter your sex assigned at birth (M/F):", ValidatorType.SEX_AT_BIRTH)

    age_of_retirement = get_input("Please enter your expected age of retirement (only as a whole number):",
                                  ValidatorType.AGE_OF_RETIREMENT, current_age)

    current_age_of_retirement = int(age_of_retirement)

    if sex_at_birth.lower()[:1] == "m":
        sex = SexAtBirth.MALE
    else:
        sex = SexAtBirth.FEMALE

    return UserInfo(name, current_age, sex, current_age_of_retirement)


if __name__ == "__main__":
    user_info = get_user_info_from_inputs()

    life_expectancy_calculator = LifeExpectancyCalculator(user_info)
    user_info = life_expectancy_calculator.calculate_for_user()

    asset_allocation_strategizer = AssetAllocationStrategizer(user_info)
    result_table = asset_allocation_strategizer.calculate_for_user()

    print(result_table)
