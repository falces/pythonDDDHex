from Application.CountryService import CountryService

class CountryController:
    def __init__(self, CountryService: CountryService):
        self.countryService = CountryService

    def getCountries(self):
        return self.countryService.getAllCountries()