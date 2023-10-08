# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import AgeValidator


class TestAgeValidator(TestCase):
    def test_with_valid_age(self):
        validator = AgeValidator("40")
        result, message = validator.validate()
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_empty_age(self):
        validator = AgeValidator(" ")
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Age is empty")

    def test_with_invalid_string(self):
        validator = AgeValidator("vfb")
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Value is not an integer")
