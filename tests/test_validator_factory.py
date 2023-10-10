# Import standard libraries
from unittest import TestCase

# Import local modules
from validators import ValidatorFactory, ValidatorType, NameValidator


class TestValidatorFactory(TestCase):
    def test_valid_factory_call(self):
        factory = ValidatorFactory()
        validator = factory.get_validator(ValidatorType.NAME)
        self.assertIsInstance(validator, NameValidator)

    def test_invalid_factory_call(self):
        factory = ValidatorFactory()
        with self.assertRaises(ValueError) as exception_context:
            factory.get_validator(99)
        self.assertEqual(
            str(exception_context.exception),
            "Invalid Validator Type"
        )
