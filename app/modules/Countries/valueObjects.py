from Shared.Domain.ValueObjects.StringValueObject import StringValueObject
from Shared.Domain.ValueObjects.IdValueObject import IdValueobject
from .exceptions import *
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

class IdCountry(IdValueobject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(
        value: id,
    ) -> Self:
        return IdCountry(value)