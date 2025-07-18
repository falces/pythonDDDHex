from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from modules.StatusGroups.entities import StatusGroup
from modules.StatusGroups.dto import StatusGroupDTO, StatusDTO
from app import signals, app
import uuid

class StatusService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def getAllStatusGroups(
        self,
        resultsInFile: bool = False,
    ) -> list:
        statusGroups  = self.repository.findAll()

        for statusGroup in statusGroups:
            statusGroup.statuses = []
            statuses = self.repository.findStatusesIdsByStatusGroupId(statusGroup.id)
            for status in statuses:
                status = self.repository.findById(status.status_id)
                statusGroup.statuses.append(status)

        return [statusGroup.toDict() for statusGroup in statusGroups]



    def addStatusGroup(
        self,
        statusGroupDTO: StatusGroupDTO,
    ):
        statusGroup = StatusGroup(
            id = statusGroupDTO.id,
            key = statusGroupDTO.key,
            description = statusGroupDTO.description,
            statuses = statusGroupDTO.statuses,
        )

        self.repository.save(statusGroup)

    def importAllStatusGroups(
        self,
        resultsInFile: bool = False,
    ) -> list:
        statusGroupsReceived = self.repository.getAllStatusGroups(resultsInFile)
        statusGroups = []
        for statusGroupReceived in statusGroupsReceived:
            statusGroup = {
                'id':  statusGroupReceived['id'],
                'group_key': statusGroupReceived['group_key'],
                'description': statusGroupReceived['description'],
                'status': [],
            }

            try:
                statusesReceived = self.repository.getStatusByStatusGroup(statusGroupReceived['id'], resultsInFile)
                for statusReceived in statusesReceived:
                    status = StatusDTO(
                        id = statusReceived['id'],
                        code = statusReceived['code'],
                        description = statusReceived['description'],
                        shortDescription = statusReceived['short_description'],
                        statusGroupId = statusGroupReceived['id'],
                    )
                    statusGroup['status'].append(status.toDict())
            except Exception as e:
                pass

            signals['new_status_group_received'].send(
                sender = uuid.uuid4().hex,
                message = statusGroup,
            )

            statusGroups.append(statusGroup)

        return statusGroups