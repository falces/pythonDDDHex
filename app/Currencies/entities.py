from Shared.Domain.Entities.EntityBase import AggregateRootBase
from app import db

class Currency(AggregateRootBase):
    def __init__(
        self,
        id: int,
        isoCode: str,
        description: str,
        active: bool,
    ):
        self.id = id
        self.isoCode = isoCode
        self.description = description
        self.active = active

        self.model = CurrencyModel(
            id=self.id,
            isoCode=self.isoCode,
            description=self.description,
            active=self.active,
        )

    def toDict(self) -> list:
        return self.model.toDict()

class CurrencyModel(db.Model):
    __tablename__ = 'currencies'

    id = db.Column(db.Integer, primary_key=True)
    isoCode = db.Column(db.String(3), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    active = db.Column(db.Boolean, unique=False, nullable=False)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "isoCode": self.isoCode,
            "description": self.description,
            "active": self.active,
        }