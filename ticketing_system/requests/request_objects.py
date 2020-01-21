from abc import ABC, abstractmethod


class InvalidRequestObject:

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return bool(self.errors)

    def __bool__(self):
        return False


class ValidRequestObject(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, adict):
        pass

    def __bool__(self):
        return True
