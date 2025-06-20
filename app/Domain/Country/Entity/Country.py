from Domain.Country.ValueObjects.IdCountry import IdCountry
from Domain.Country.ValueObjects.CountryCode import CountryCode

class Country:
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
        
    def toDict(self) -> dict:
        return {
            "id": self.id.getValue(),
            "name": self.name,
            "code": self.code.getValue(),
            "hasSubzone": self.hasSubzone,
            "isEUMember": self.isEUMember,
        }