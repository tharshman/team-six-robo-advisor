# Import system modules
from unittest import TestCase

# Import local modules
from services import LifeExpectancyCalculator
from models import UserInfo, SexAtBirth


class TestLifeExpectancyCalculator(TestCase):
    def test_with_valid_age_and_male_sex(self):
        user = UserInfo("Vin", 49, SexAtBirth.MALE, 70)
        calc = LifeExpectancyCalculator(user, "life_expectancy_db.csv")
        user = calc.calculate_for_user()
        self.assertEqual(user.life_expectancy, 29)
        self.assertEqual(user.expected_age_of_death, 78)

    def test_with_valid_age_and_female_sex(self):
        user = UserInfo("Jen", 51, SexAtBirth.FEMALE, 70)
        calc = LifeExpectancyCalculator(user, "life_expectancy_db.csv")
        user = calc.calculate_for_user()
        self.assertEqual(user.life_expectancy, 31)
        self.assertEqual(user.expected_age_of_death, 82)

    def test_with_invalid_age(self):
        user = UserInfo("Jen", 200, SexAtBirth.FEMALE, 205)
        calc = LifeExpectancyCalculator(user, "life_expectancy_db.csv")
        with self.assertRaises(ValueError) as exception_context:
            user = calc.calculate_for_user()
        self.assertEqual(
            str(exception_context.exception),
            "No data available for age 200"
        )

    def test_with_invalid_sex(self):
        user = UserInfo("Jen", 51, 99, 70)
        calc = LifeExpectancyCalculator(user, "life_expectancy_db.csv")
        with self.assertRaises(ValueError) as exception_context:
            user = calc.calculate_for_user()
        self.assertEqual(
            str(exception_context.exception),
            "No data available for sex 99"
        )
