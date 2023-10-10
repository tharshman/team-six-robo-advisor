# Import local modules
from services import LifeExpectancyCalculator, AssetAllocationStrategizer
from validators import ValidatorFactory, ValidatorType
from models import UserInfo, SexAtBirth


def get_input(prompt: str, validator_type: ValidatorType, second_value: any = None) -> str:
    value_is_valid = False
    value = None
    validator = ValidatorFactory.get_validator(validator_type)
    while not value_is_valid:
        value = input(prompt)
        value_is_valid, error_message = validator.validate(value, second_value)
        if not value_is_valid:
            print(error_message)
            print("Let's try that again")
    return value


def get_user_info_from_inputs() -> UserInfo:
    name = get_input("Please enter your name:", ValidatorType.NAME)

    age = get_input("Please enter your age (only as a whole number):", ValidatorType.AGE)
    current_age = int(age)

    sex_at_birth = get_input("Please enter your sex assigned at birth (M/F):", ValidatorType.SEX_AT_BIRTH)
    if sex_at_birth.lower()[:1] == "m":
        current_sex_at_birth = SexAtBirth.MALE
    else:
        current_sex_at_birth = SexAtBirth.FEMALE

    age_of_retirement = get_input("Please enter your expected age of retirement (only as a whole number):",
                                  ValidatorType.AGE_OF_RETIREMENT, current_age)

    current_age_of_retirement = int(age_of_retirement)

    return UserInfo(name, current_age, current_sex_at_birth, current_age_of_retirement)


if __name__ == "__main__":
    LIFE_EXPECTANCY_DATA_FILE = "life_expectancy_db.csv"

    user_info = get_user_info_from_inputs()

    life_expectancy_calculator = LifeExpectancyCalculator(user_info, LIFE_EXPECTANCY_DATA_FILE)
    user_info = life_expectancy_calculator.calculate_for_user()

    asset_allocation_strategizer = AssetAllocationStrategizer(user_info)
    result_table = asset_allocation_strategizer.calculate_for_user()

    for row in result_table:
        print(f"YTR: {row.years_to_retirement}   Stock: {row.percent_in_stock}   Bonds: {row.percent_in_bonds}")
