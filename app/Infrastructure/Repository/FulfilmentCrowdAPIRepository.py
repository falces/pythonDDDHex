from flask import current_app
from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Shared.Infrastructure.APITools import APITools

class FulfilmentCrowdAPIRepository(AbstractCountryRepository):
    def __init__(self):
        self.api_tools = APITools()
        self.url = '/countries'
        self.apiKey = current_app.config['API_KEY']
    
    def getAllCountries(self) -> list:      
        data = self.api_tools.get(
            url = self.url,
            headers = {
                        'fulfilmentcrowd-api-key': self.apiKey
                      },
        )
        data = data.json()
        return data