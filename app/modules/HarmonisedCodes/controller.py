from flask import Blueprint, request
from modules.HarmonisedCodes.service import HarmonisedCodesService
from Shared.Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from modules.HarmonisedCodes.repository import HarmonisedCodesRepository

harmonisedCodesController = Blueprint('harmonisedCodesController', __name__)

@harmonisedCodesController.route('/import', methods=['POST'])
def importAllHarmonisedCodes():
    harmonisedCodesService = HarmonisedCodesService(FulfilmentCrowdAPIRepository)
    return harmonisedCodesService.syncHarmonisedCodes()

@harmonisedCodesController.route('/', methods=['GET'])
def getAllHarmonisedCodes():
    harmonisedCodesService = HarmonisedCodesService(HarmonisedCodesRepository)
    return harmonisedCodesService.getAllHarmonisedCodes()