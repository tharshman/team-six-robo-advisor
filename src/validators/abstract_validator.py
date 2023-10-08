from abc import ABCMeta, abstractmethod


class AbstractValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self) -> (bool, str):
        pass
