from flask import Blueprint, request
from app import signals
from modules.StatusGroups.service import StatusService
from modules.StatusGroups.dto import StatusGroupDTO
from Shared.Infrastructure.Repository.FulfilmentCrowdAPIRepository import FulfilmentCrowdAPIRepository
from modules.StatusGroups.repository import StatusGroupRepository


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

@signals['new_status_group_received'].connect
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
