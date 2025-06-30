from abc import ABC, abstractmethod


class AbstractEntityRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save(self):
        pass