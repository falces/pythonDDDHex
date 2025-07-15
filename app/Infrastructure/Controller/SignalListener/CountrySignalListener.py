from app import signals
from flask import Blueprint
from Infrastructure.Repository.CountryRepository import CountryRepository
from Application.CountryService import CountryService
from Application.DTO.CountryDTO import CountryDTO

countrySignalListener = Blueprint('countrySignalListener', __name__)

class CountrySignalListener():

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