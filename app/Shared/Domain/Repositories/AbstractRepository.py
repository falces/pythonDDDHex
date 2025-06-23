from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    
    @abstractmethod
    def getAllCountries(self) -> list:
        return []