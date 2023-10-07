# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import AgeValidator


class TestAgeValidator(TestCase):
    def test_with_valid_age(self):
        result, message = AgeValidator().validate("40")
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_empty_age(self):
        result, message = AgeValidator().validate(" ")
        self.assertFalse(result)
        self.assertEqual(message, "Age is empty")

    def test_with_invalid_string(self):
        result, message = AgeValidator().validate("vfb")
        self.assertFalse(result)
        self.assertEqual(message, "Value is not an integer")
