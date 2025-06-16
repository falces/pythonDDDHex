from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Domain.Country.Entity.Country import Country

class CountryService:
    def __init__(
        self,
        countryRepository: AbstractCountryRepository
    ):
        self.countryRepository = countryRepository
        
    def getAllCountries(self) -> list:
        countries = self.countryRepository.getAllCountries()
        myCountries = []
        for country in countries:
            # Assuming each country is a dictionary with the necessary fields
            myCountry = Country(
                id=country['id'],
                name=country['name'],
                code=country['code'],
                hasSubzone=country['hasSubzone'],
                isEUMember=country['isEUMember']
            )
            myCountries.append(myCountry.toDict)
        return countries