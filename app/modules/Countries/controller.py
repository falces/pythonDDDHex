from app import signals
from flask import Blueprint, request
from modules.Countries.service import CountryService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from modules.Countries.repository import CountryRepository
from Infrastructure.Controller.ControllerBase import ControllerBase
from .dto import CountryDTO


countryController = Blueprint('countryController', __name__)

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
    return {
        'message': str(
            len(countryService.importCountries())
        ) + ' Countries updated successfully'
    }, 201

@signals['new_country_received'].connect
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