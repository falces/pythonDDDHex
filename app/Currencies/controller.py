from flask import Blueprint
from app import signals
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from .repository import CurrencyRepository
from .service import *


currenciesController = Blueprint('currenciesController', __name__)

@currenciesController.route('/import', methods=['POST'])
def importAllCurrencies():
    return {
        'message': str(
            len(
                importCurrenciesService(FulfilmentCrowdAPIRepository())
            )
        ) + ' Currencies imported successfully'
    }, 201

@currenciesController.route('/', methods=['GET'])
def getAllCurrencies():
    return {
        'currencies': [
            currency.toDict() for currency in CurrencyRepository().findAll()
        ]
    }, 200

@signals['new_currency_received'].connect
def newCurrencyReceived(
    self,
    sender: str,
    message: dict,
):
    saveCurrency(
        repository = CurrencyRepository(),
        currencyDTO = {
            "id": message['id'],
            "isoCode": message['isoCode'],
            "description": message['description'],
            "active": message['active'],
        }
    )