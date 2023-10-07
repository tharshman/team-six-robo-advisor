# Import standard libraries
from unittest import TestCase

# Import local modules
from validators.age_of_retirement_validator import AgeOfRetirementValidator


class TestAgeOfRetirementValidator(TestCase):
    def test_with_valid_age_of_retirement(self):
        result, message = AgeOfRetirementValidator.validate("70", 49)
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_invalid_retirement_age_string(self):
        result, message = AgeOfRetirementValidator.validate("vin", 49)
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_float(self):
        result, message = AgeOfRetirementValidator.validate("65.5", 49)
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_value(self):
        result, message = AgeOfRetirementValidator.validate("30", 49)
        self.assertFalse(result)
        self.assertEqual(message, "The retirement age needs to be in the future")
