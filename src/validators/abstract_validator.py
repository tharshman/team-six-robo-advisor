from abc import ABCMeta, abstractmethod


class AbstractValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, value: str, second_value=None) -> (bool, str):
        pass
