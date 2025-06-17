from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Domain.Country.Entity.Country import Country

class CountryService:
    def __init__(
        self,
        countryRepository: AbstractCountryRepository
    ):
        self.countryRepository = countryRepository()
        
    def getAllCountries(self) -> list:
        countries = self.countryRepository.getAllCountries()
        myCountries = []
        for country in countries:
            myCountry = Country(
                id=country['id'],
                name=country['description'],
                code=country['country_code'],
                hasSubzone=country['subdivisions_in_use'],
                isEUMember=country['eu_member']
            )
            country = myCountry.toDict()
            myCountries.append(country)
        return myCountries