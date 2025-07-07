from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.Country.CountryModel import CountryModel
from Domain.Country.Country import Country
from app import db


class CountryRepository (AbstractRepository):
    def __init__(self):
        self.model = CountryModel()

    def save(
        self,
        country: Country,
    ):
        db.session.add(country.getModel())
        db.session.commit()

    def findAll(
        self,
    ) -> list:
        return self.model.query.all()

    def findById(
        self,
        id: int,
    ) -> Country:
        return self.model.query.filter_by(id=id).first()