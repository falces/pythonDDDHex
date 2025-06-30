from flask import Blueprint, request
from Application.StatusService import StatusService
from Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from Infrastructure.Repository.StatusGroupRepository import StatusGroupRepository
from Domain.StatusGroups.StatusGroupDTO import StatusGroupDTO

from app import signals

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

@signals['new_status_group'].connect
def newStatusGroupListener(
    self,
    sender: str,
    message: dict,
):
    statusGroupDTO = StatusGroupDTO(
        id = message['id'],
        key = message['group_key'],
        description = message['description'],
        statuses = message['status'],
    )

    statusService = StatusService(StatusGroupRepository)
    statusService.addStatusGroup(statusGroupDTO)