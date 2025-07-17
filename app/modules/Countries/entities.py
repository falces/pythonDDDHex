from .valueObjects import *
from Shared.Domain.Entities.EntityBase import AggregateRootBase
from app import db

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

class CountryModel(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    hasSubzone = db.Column(db.Boolean, unique=False, nullable=False)
    isEUMember = db.Column(db.Boolean, unique=False, nullable=False)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "hasSubzone": self.hasSubzone,
            "isEUMember": self.isEUMember,
        }