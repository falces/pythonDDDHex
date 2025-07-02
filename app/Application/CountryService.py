from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.Country.Country import Country
from Domain.Country.ValueObjects.IdCountry import IdCountry
from Domain.Country.ValueObjects.CountryCode import CountryCode
from app import db, app, signals
import uuid
from Application.DTO import CountryDTO

class CountryService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def addCountry(
        self,
        countryDTO: CountryDTO,
    ):
        country = Country(
            id =         IdCountry.create(countryDTO.id),
            name =       countryDTO.name,
            code =       CountryCode.create(countryDTO.code),
            hasSubzone = countryDTO.hasSubzone,
            isEUMember = countryDTO.isEUMember,
        )

        self.repository.save(country)

    def getAllCountries(
        self,
        resultsInFile: bool = False,
    ) -> list:
        allCountries = self.repository.findAll()
        app.logger.info("Total countries retrieved from database: %s", len(allCountries))

        countries = []
        for country in allCountries:
            countries.append(country.toDict())

        return countries

    def importCountries(
        self,
        resultsInFile: bool = False,
    ) -> list:
        receivedCountries = self.repository.getAllCountries(resultsInFile)
        countries = []
        for receivedCountry in receivedCountries:
            country = Country(
                id =         IdCountry.create(receivedCountry['id']),
                name =       receivedCountry['description'],
                code =       CountryCode.create(receivedCountry['country_code']),
                hasSubzone = receivedCountry['subdivisions_in_use'],
                isEUMember = receivedCountry['eu_member'],
            )

            signals['new_country'].send(
                sender=uuid.uuid4().hex,
                message=country.toDict(),
            )

            countries.append(country.toDict())
        app.logger.info("Total countries imported: %s", len(countries))
        return countries