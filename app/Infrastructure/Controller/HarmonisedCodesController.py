from flask import Blueprint, request
from Application.HarmonisedCodesService import ImportHarmonisedCodesService, GetHarmonisedCodesService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

harmonisedCodesController = Blueprint('harmonisedCodesController', __name__)

@harmonisedCodesController.route('/import', methods=['POST'])
def importAllHarmonisedCodes():
    harmonisedCodesService = ImportHarmonisedCodesService(FulfilmentCrowdAPIRepository)
    return harmonisedCodesService.syncHarmonisedCodes()

@harmonisedCodesController.route('/', methods=['GET'])
def getAllHarmonisedCodes():
    harmonisedCodesService = GetHarmonisedCodesService(FulfilmentCrowdAPIRepository)
    return harmonisedCodesService.getAllHarmonisedCodes()