from flask import Blueprint
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getAllCountries():
    countries = CountryService(FulfilmentCrowdAPIRepository)   
    return countries.getAllCountries()