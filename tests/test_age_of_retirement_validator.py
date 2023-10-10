# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import AgeOfRetirementValidator


class TestAgeOfRetirementValidator(TestCase):
    def test_with_valid_age_of_retirement(self):
        validator = AgeOfRetirementValidator()
        result, message = validator.validate("70", 49)
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_invalid_retirement_age_string(self):
        validator = AgeOfRetirementValidator()
        result, message = validator.validate("vin", 49)
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_float(self):
        validator = AgeOfRetirementValidator()
        result, message = validator.validate("65.5", 49)
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement should be a whole number")

    def test_with_invalid_retirement_age_value(self):
        validator = AgeOfRetirementValidator()
        result, message = validator.validate("30", 49)
        self.assertFalse(result)
        self.assertEqual(message, "The retirement age needs to be in the future")

    def test_with_out_of_range_value(self):
        validator = AgeOfRetirementValidator()
        result, message = validator.validate("700", 49)
        self.assertFalse(result)
        self.assertEqual(message, "Age of retirement range needs to be between 21 and 100")
