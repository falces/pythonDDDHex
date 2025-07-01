from flask import Blueprint, request, make_response
from Application.CountryService import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from app import signals
from Domain.Country.CountryDTO import CountryDTO
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

    @signals['new_country'].connect
    def newCountryListener(
        self,
        sender: str,
        message: dict,
    ):
        countryDTO = CountryDTO(
            id = message['id'],
            name = message['name'],
            code = message['code'],
            hasSubzone = message['hasSubzone'],
            isEUMember = message['isEUMember'],
        )

        statusService = CountryService(CountryRepository)
        statusService.addCountry(countryDTO)