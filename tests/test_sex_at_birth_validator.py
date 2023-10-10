# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import SexAtBirthValidator


class TestSexAtBirthValidator(TestCase):
    def test_with_valid_sex(self):
        valid_sexes = ['m', 'F', 'Male', 'FEMALE']
        for s in valid_sexes:
            with self.subTest(msg=f"Validate {s} with SexAtBirthValidator", s=s):
                validator = SexAtBirthValidator()
                result, message = validator.validate(s)
                self.assertTrue(result)
                self.assertIsNone(message)

    def test_with_empty_sex(self):
        validator = SexAtBirthValidator()
        result, message = validator.validate(" ")
        self.assertFalse(result)
        self.assertEqual(message, "Sex is empty")

    def test_with_too_long_sex(self):
        validator = SexAtBirthValidator()
        result, message = validator.validate("alien")
        self.assertFalse(result)
        self.assertEqual(message, "Invalid value for sex")
