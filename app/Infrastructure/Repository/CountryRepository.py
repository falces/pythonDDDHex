from abc import ABC
from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository

class CountryRepository(AbstractCountryRepository):
    
    def getAllCountries(self) -> list:
        return [
            {
                "id": 1,
                "name": "United States",
                "code": "US",
                "hasSubzone": False,
                "isEUMember": False,
            },
            {
                "id": 2,
                "name": "Germany",
                "code": "DE",
                "hasSubzone": True,
                "isEUMember": True,
            },
            {
                "id": 3,
                "name": "France",
                "code": "FR",
                "hasSubzone": True,
                "isEUMember": True,
            },
        ]