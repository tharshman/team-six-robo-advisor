# Import third-party modules
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel

# Import local modules
from services import LifeExpectancyCalculator, AssetAllocationStrategizer
from validators import ValidatorFactory, ValidatorType
from models import UserInfo, SexAtBirth, AssetAllocationTable


def get_input(prompt: str, validator_type: ValidatorType, second_value: any = None) -> str:
    value_is_valid = False
    value = None
    validator = ValidatorFactory.get_validator(validator_type)
    while not value_is_valid:
        value = console.input(prompt)
        value_is_valid, error_message = validator.validate(value, second_value)
        if not value_is_valid:
            console.print(error_message, style="red")
            console.print("Let's try that again")
    return value


def get_user_info_from_inputs() -> UserInfo:
    name = get_input("Please enter your name: ", ValidatorType.NAME)

    age = get_input("Please enter your age (only as a whole number): ", ValidatorType.AGE)
    current_age = int(age)

    sex_at_birth = get_input("Please enter your sex assigned at birth (M/F): ", ValidatorType.SEX_AT_BIRTH)
    if sex_at_birth.lower()[:1] == "m":
        current_sex_at_birth = SexAtBirth.MALE
    else:
        current_sex_at_birth = SexAtBirth.FEMALE

    age_of_retirement = get_input("Please enter your expected age of retirement (only as a whole number): ",
                                  ValidatorType.AGE_OF_RETIREMENT, current_age)

    current_age_of_retirement = int(age_of_retirement)

    return UserInfo(name, current_age, current_sex_at_birth, current_age_of_retirement)


def draw_result_table(data: AssetAllocationTable, user: UserInfo):
    table = Table(title=f"Asset Allocation Strategy for {user.name}")

    table.add_column("Years to Retirement\n(Years before Target Date)", justify="right", no_wrap=False)
    table.add_column("Stocks", justify="right")
    table.add_column("Bonds", justify="right")

    for row in data:
        table.add_row(f"{row.years_to_retirement}", f"{row.percent_in_stock}%", f"{row.percent_in_bonds}%")

    console.print(table)


if __name__ == "__main__":
    console = Console(color_system="standard")

    LIFE_EXPECTANCY_DATA_FILE = "life_expectancy_db.csv"

    user_info = get_user_info_from_inputs()
    try:
        life_expectancy_calculator = LifeExpectancyCalculator(user_info, LIFE_EXPECTANCY_DATA_FILE)
        user_info = life_expectancy_calculator.calculate_for_user()

        asset_allocation_strategizer = AssetAllocationStrategizer(user_info)
        result_table = asset_allocation_strategizer.calculate_for_user()

        console.print()

        print(
            Panel(
                f"{user_info.name}, your life expectancy is {user_info.life_expectancy} years",
                title="Life expectancy"
            )
        )

        draw_result_table(result_table, user_info)

    except ValueError as err:
        console.print(err, style="red")
