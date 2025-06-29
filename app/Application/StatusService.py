from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.StatusGroups.StatusGroup import StatusGroup
from app import db

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
        pass

    def importAllStatusGroups(
        self,
        resultsInFile: bool = False,
    ) -> list:
        statusGroupsReceived = self.repository.getAllStatusGroups(resultsInFile)
        statusGroups = []
        for statusGroupReceived in statusGroupsReceived:
            statusGroup = StatusGroup(
                id = statusGroupReceived['id'],
                key = statusGroupReceived['group_key'],
                description = statusGroupReceived['description'],
                status = [],
            )

            try:
                statusesReceived = self.repository.getStatusForGroup(statusGroupReceived['id'], resultsInFile)
                for statusReceived in statusesReceived:
                    statusGroup.addStatus(
                        id=statusReceived["id"],
                        code=statusReceived["code"],
                        description=statusReceived["description"],
                        shortDescription=statusReceived["short_description"],
                    )
            except Exception as e:
                pass

            db.session.add(statusGroup.model)
            db.session.commit()

            statusGroup = statusGroup.toDict()
            statusGroups.append(statusGroup)
        return statusGroups