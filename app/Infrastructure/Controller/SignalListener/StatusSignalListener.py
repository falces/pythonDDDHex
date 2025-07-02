from app import signals
from flask import Blueprint
from Infrastructure.Repository.StatusGroupRepository import StatusGroupRepository
from Application.StatusService import StatusService
from Application.DTO.StatusGroupDTO import StatusGroupDTO

statusSignalListener = Blueprint('statusSignalListener', __name__)

class StatusSignalListener():

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