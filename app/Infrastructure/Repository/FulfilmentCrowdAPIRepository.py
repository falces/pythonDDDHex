from flask import current_app
from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Shared.Infrastructure.APITools import APITools

class FulfilmentCrowdAPIRepository(AbstractCountryRepository):
    def __init__(self):
        self.api_tools = APITools()
        self.url = '/countries'
        self.apiKey = current_app.config['API_KEY']
    
    def getAllCountries(self, resultsInFile: bool = False) -> list:

        fileName = None
        if resultsInFile:
            fileName = 'countries.xlsx'
        
        data = self.api_tools.get(
            url = self.url,
            headers = {
                        'fulfilmentcrowd-api-key': self.apiKey
                      },
            resultsInFile=resultsInFile,
            fileName=fileName
        )
        data = data.json()
        return data