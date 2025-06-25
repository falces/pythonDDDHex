from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.Country.Country import Country
from Domain.Country.ValueObjects.IdCountry import IdCountry
from Domain.Country.ValueObjects.CountryCode import CountryCode
from app import db, app
from Domain.Country.CountryModel import CountryModel

class GetCountryService:
    def __init__(
        self,
        countryRepository: AbstractRepository,
    ):
        self.countryRepository = countryRepository()

    def getAllCountries(
        self,
        resultsInFile: bool = False,
    ) -> list:

        allCountries = CountryModel.query.all()
        countries = []

        for country in allCountries:
            countries.append(country.toDict())

        return countries

class PostCountryService:
    def __init__(
        self,
        countryRepository: AbstractRepository,
    ):
        self.countryRepository = countryRepository()

    def importAllCountries(
        self,
        resultsInFile: bool = False,
    ) -> list:
        receivedCountries = self.countryRepository.getAllCountries(resultsInFile)
        countries = []
        for receivedCountry in receivedCountries:
            country = Country(
                id =         IdCountry.create(receivedCountry['id']),
                name =       receivedCountry['description'],
                code =       CountryCode.create(receivedCountry['country_code']),
                hasSubzone = receivedCountry['subdivisions_in_use'],
                isEUMember = receivedCountry['eu_member'],
            )

            db.session.add(country.model)
            db.session.commit()

            countries.append(country.toDict())
        app.logger.info("Total countries imported: %s", len(countries))
        return {'message': str(len(countries)) + ' Countries updated successfully'}, 201