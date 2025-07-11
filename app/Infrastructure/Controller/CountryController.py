from flask import Blueprint, request
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from Infrastructure.Repository.CountryRepository import CountryRepository
from Infrastructure.Controller.ControllerBase import ControllerBase


countryController = Blueprint('countryController', __name__)

class CountryController():

    @countryController.route('/', methods=['GET'])
    def getAllCountries():
        resultsInFile = request.args.get('resultsInFile')
        countryService = CountryService(CountryRepository)

        return ControllerBase.formatResponse(
            countryService.getAllCountries(resultsInFile),
            200,
        )

    @countryController.route('/import', methods=['POST'])
    def postAllCountries():
        countryService = CountryService(FulfilmentCrowdAPIRepository)
        return {'message': str(len(countryService.importCountries())) + ' Countries updated successfully'}, 201