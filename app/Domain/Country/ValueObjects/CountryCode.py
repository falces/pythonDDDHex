from Shared.Domain.ValueObjects.StringValueObject import StringValueObject
from Domain.Country.Exceptions.IncorrectCountryCodeException import IncorrectCountryCodeException
from typing import Self

class CountryCode(StringValueObject):
    def __init__(
        self,
        value:str,
    ):
        if len(value) != 2:
            raise IncorrectCountryCodeException(value)
        
        super().__init__(value = value)

    @staticmethod
    def create(
        value: str,
    ) -> Self:
        return CountryCode(value)