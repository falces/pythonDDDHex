from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from .entities import Currency, CurrencyModel
from app import db


class CurrencyRepository (AbstractRepository):
    def __init__(self):
        self.model = CurrencyModel()

    def save(
        self,
        currency: Currency,
    ):
        db.session.add(currency.getModel())
        db.session.commit()

    def findAll(
        self,
    ) -> list:
        return self.model.query.all()

    def findById(
        self,
        id: int,
    ) -> Currency:
        return self.model.query.filter_by(id=id).first()