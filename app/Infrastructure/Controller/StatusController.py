from flask import Blueprint, request
from Application.StatusService import StatusService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository

statusController = Blueprint('statusController', __name__)

@statusController.route('/', methods=['GET'])
def getAllStatusGroups():
    resultsInFile = request.args.get('resultsInFile')
    status = StatusService(FulfilmentCrowdAPIRepository)
    return status.getAllStatusGroups(resultsInFile)

@statusController.route('/', methods=['POST'])
def imporptAllStatusGroups():
    resultsInFile = request.args.get('resultsInFile')
    status = StatusService(FulfilmentCrowdAPIRepository)
    return status.importAllStatusGroups(resultsInFile)