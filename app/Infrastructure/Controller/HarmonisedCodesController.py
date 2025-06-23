from flask import Blueprint, request
from Application.HarmonisedCodesService import HarmonisedCodesService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

harmonisedCodesController = Blueprint('harmonisedCodesController', __name__)

@harmonisedCodesController.route('/import', methods=['POST'])
def importAllHarmonisedCodes():
    harmonisedCodesService = HarmonisedCodesService(FulfilmentCrowdAPIRepository)
    return harmonisedCodesService.syncHarmonisedCodes()