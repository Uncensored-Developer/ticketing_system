from abc import ABC, abstractmethod


class Base(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, adict):
        pass

    @abstractmethod
    def to_dict(self):
        pass
