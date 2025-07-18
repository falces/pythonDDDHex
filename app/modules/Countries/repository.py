from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from .entities import Country, CountryModel, CountriesToCurrenciesModel
from modules.Countries.entities import Country
from app import db
from flask import current_app as app


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

    def findCurrencyByCountry(
        self,
        country: str,
    ) -> str:
        model = CountriesToCurrenciesModel()
        try:
            return model.query.filter_by(
                country = country,
            ).first().currency
        except:
            app.logger.info("No currency found for country: %s", country)
            return None