from flask import Blueprint, request
from Application.CountryService import GetCountryService, PostCountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getAllCountries():
    resultsInFile = request.args.get('resultsInFile')
    countriesService = GetCountryService(FulfilmentCrowdAPIRepository)
    return countriesService.getAllCountries(resultsInFile)

@countryController.route('/', methods=['POST'])
def postAllCountries():
    countriesService = PostCountryService(FulfilmentCrowdAPIRepository)
    return countriesService.importAllCountries()