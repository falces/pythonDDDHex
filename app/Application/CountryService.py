from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Domain.Country.Entity.Country import Country
from Domain.Country.ValueObjects.IdCountry import IdCountry
from Domain.Country.ValueObjects.CountryCode import CountryCode

class CountryService:
    def __init__(
        self,
        countryRepository: AbstractCountryRepository,
    ):
        self.countryRepository = countryRepository()

    def getAllCountries(
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
            ).toDict()
            countries.append(country)
        return countries