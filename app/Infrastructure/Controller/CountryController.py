from flask import Blueprint, request
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from Shared.Domain.Exceptions.ApiKeyNotProvidedException import ApiNotProvidedException

countryController = Blueprint('countryController', __name__)

@countryController.route('/', methods=['GET'])
def getAllCountries():
    apiKey = request.headers.get('apiKey')
    if apiKey:
        if apiKey == 'hJkhabWB24LXw5VELGwS3dDj2':
            resultsInFile = request.args.get('resultsInFile')
            countriesService = CountryService(FulfilmentCrowdAPIRepository)
            return countriesService.getAllCountries(resultsInFile)
        else:
            raise ApiNotProvidedException()
    else:
        raise ApiNotProvidedException()