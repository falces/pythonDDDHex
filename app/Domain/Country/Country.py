from Domain.Country.ValueObjects.IdCountry import IdCountry
from Domain.Country.ValueObjects.CountryCode import CountryCode
from Shared.Domain.Entities.EntityBase import AggregateRootBase
from Domain.Country.CountryModel import CountryModel

class Country(AggregateRootBase):
    def __init__(
        self,
        id: IdCountry,
        name: str,
        code: CountryCode,
        hasSubzone: bool = False,
        isEUMember: bool = False,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.hasSubzone = hasSubzone
        self.isEUMember = isEUMember

        self.model = CountryModel(
            id=self.id.getValue(),
            name=self.name,
            code=self.code.getValue(),
            hasSubzone=self.hasSubzone,
            isEUMember=self.isEUMember,
        )

    def toDict(self) -> dict:
        return self.model.toDict()