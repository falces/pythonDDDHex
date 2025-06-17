from flask import Blueprint, request
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getAllCountries():
    resultsInFile = request.args.get('resultsInFile')
    countries = CountryService(FulfilmentCrowdAPIRepository)   
    return countries.getAllCountries(resultsInFile)