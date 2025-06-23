from flask import Blueprint, request
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getAllCountries():
    resultsInFile = request.args.get('resultsInFile')
    countriesService = CountryService(FulfilmentCrowdAPIRepository)
    return countriesService.getAllCountries(resultsInFile)