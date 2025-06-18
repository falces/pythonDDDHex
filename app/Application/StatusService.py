from Domain.Country.Repository.AbstractCountryRepository import AbstractCountryRepository
from Domain.Status.Entity.StatusGroup import StatusGroup

class StatusService:
    def __init__(
        self,
        repository: AbstractCountryRepository,
    ):
        self.repository = repository()
        
    def getAllStatusGroups(
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
            
            statusesReceived = self.repository.getStatusForGroup(statusGroupReceived['id'], resultsInFile)
            for statusReceived in statusesReceived:
                statusGroup.addStatus(
                    id=statusReceived["id"],
                    code=statusReceived["code"],
                    description=statusReceived["description"],
                    shortDescription=statusReceived["short_description"],
                )
                
            statusGroup = statusGroup.toDict()
            statusGroups.append(statusGroup)
        return statusGroups