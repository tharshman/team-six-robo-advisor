# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import NameValidator


class TestNameValidator(TestCase):
    def test_with_valid_name(self):
        validator = NameValidator("Vincent Bortone")
        result, message = validator.validate()
        self.assertTrue(result)
        self.assertIsNone(message)

    def test_with_empty_name(self):
        validator = NameValidator(" ")
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Name is empty")

    def test_with_too_long_name(self):
        validator = NameValidator("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertEqual(message, "Name is too long")
