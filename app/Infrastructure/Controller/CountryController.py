from flask import Blueprint

from Application.CountryService import CountryService
from Infrastructure.Repository.CountryRepository import CountryRepository

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getCountries():
    countries = CountryService(CountryRepository)   
    return countries.getAllCountries()