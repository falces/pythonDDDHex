from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Shared.Infrastructure.APITools import APITools

class FulfilmentCrowdAPIRepository(AbstractRepository):
    COUNTRIES_ENDPOINT = '/countries'
    STATUS_GROUPS_ENDPOINT = '/status_groups'
    
    def __init__(self):
        self.api_tools = APITools()
        
    def __sendGetRequest(
        self,
        endpoint: str,
        resultsInFile: bool = False,
        fileName: str = None
    ):
        return self.api_tools.get(
            endpoint = endpoint,
            resultsInFile=resultsInFile,
            fileName=fileName
        ).json()
    
    def getAllCountries(
        self,
        resultsInFile: bool = False
    ) -> list:
        fileName = None
        if resultsInFile:
            fileName = 'countries.xlsx'
        return self.__sendGetRequest(
            endpoint = self.COUNTRIES_ENDPOINT,
            resultsInFile=resultsInFile,
            fileName=fileName
        )
    
    def getAllStatusGroups(
        self,
        resultsInFile = None,
    ) -> list:
        return self.__sendGetRequest(
            endpoint = self.STATUS_GROUPS_ENDPOINT,
            resultsInFile=resultsInFile,
        )
        
    def getStatusForGroup(
        self,
        id: int,
        resultsInFile = None,
    ) -> list:
        return self.__sendGetRequest(
            endpoint = self.STATUS_GROUPS_ENDPOINT + '/' + str(id) + '/statuses',
            resultsInFile=resultsInFile,
        )