from abc import ABC, abstractmethod

class AbstractCountryRepository(ABC):
    
    @abstractmethod
    def getAllCountries(self) -> list:
        return []