from abc import ABCMeta, abstractmethod


class Utility(metaclass=ABCMeta):
    def __init__(self, description=None):
        self.description = description

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def run(self):
        pass
