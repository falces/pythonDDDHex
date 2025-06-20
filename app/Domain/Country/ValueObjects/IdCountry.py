from Shared.Domain.ValueObjects.IdValueObject import IdValueobject
from typing import Self

class IdCountry(IdValueobject):
    def __init__(self, value):
        super().__init__(value)
        
    @staticmethod
    def create(
        value: id,
    ) -> Self:
        return IdCountry(value)