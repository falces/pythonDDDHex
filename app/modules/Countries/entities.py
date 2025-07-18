from .valueObjects import *
from Shared.Domain.Entities.EntityBase import AggregateRootBase, EntityBase
from app import db

class Country(AggregateRootBase):
    def __init__(
        self,
        id: IdCountry,
        name: str,
        code: CountryCode,
        hasSubzone: bool = False,
        isEUMember: bool = False,
        currency: str = None,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.hasSubzone = hasSubzone
        self.isEUMember = isEUMember
        self.currency = currency

        self.model = CountryModel(
            id = self.id.getValue(),
            name = self.name,
            code = self.code.getValue(),
            hasSubzone = self.hasSubzone,
            isEUMember = self.isEUMember,
            currency = self.currency,
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
    currency = db.Column(db.String(3), unique=False, nullable=True)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "hasSubzone": self.hasSubzone,
            "isEUMember": self.isEUMember,
            "currency": self.currency,
        }

class CountriesToCurrencies(EntityBase):
    def __init__(
        self,
        country: str,
        currency: str,
    ):
        self.country = country
        self.currency = currency

        self.model = CountriesToCurrenciesModel(
            country=self.country,
            currency=self.currency,
        )

    def toDict(self) -> dict:
        return self.model.toDict()

class CountriesToCurrenciesModel(db.Model):
    __tablename__ = 'countries_to_currencies'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(3), unique=True, nullable=False)
    currency = db.Column(db.String(3), unique=False, nullable=True)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "country": self.country,
            "currency": self.currency,
        }