# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import AgeOfRetirementValidator


class TestAgeOfRetirementValidator(TestCase):
    def test_with_valid_age_of_retirement(self):
        validator = AgeOfRetirementValidator("70", 49)
        result, message = validator.validate()
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_invalid_retirement_age_string(self):
        validator = AgeOfRetirementValidator("vin", 49)
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_float(self):
        validator = AgeOfRetirementValidator("65.5", 49)
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_value(self):
        validator = AgeOfRetirementValidator("30", 49)
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "The retirement age needs to be in the future")
