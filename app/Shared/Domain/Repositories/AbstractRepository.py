from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def findStatusById(self):
        pass