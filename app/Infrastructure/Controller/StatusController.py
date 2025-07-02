from flask import Blueprint, request
from Application.StatusService import StatusService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from Infrastructure.Repository.StatusGroupRepository import StatusGroupRepository


statusController = Blueprint('statusController', __name__)

@statusController.route('/', methods=['GET'])
def getAllStatusGroups():
    resultsInFile = request.args.get('resultsInFile')
    statusService = StatusService(StatusGroupRepository)
    return statusService.getAllStatusGroups(resultsInFile)

@statusController.route('/import', methods=['POST'])
def imporptAllStatusGroups():
    resultsInFile = request.args.get('resultsInFile')
    status = StatusService(FulfilmentCrowdAPIRepository)
    return status.importAllStatusGroups(resultsInFile)