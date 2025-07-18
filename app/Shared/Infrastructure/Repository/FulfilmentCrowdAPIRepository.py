from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Shared.Infrastructure.APITools import APITools

class FulfilmentCrowdAPIRepository(AbstractRepository):
    COUNTRIES_ENDPOINT = '/countries'
    STATUS_GROUPS_ENDPOINT = '/status_groups'
    HARMONISED_CODES_ENDPOINT = '/harmonised_codes'
    CURRENCIES_ENDPOINT = '/currencies'

    def __init__(self):
        self.api_tools = APITools()

    def save(self):
        pass

    def findAll(self):
        pass

    def findById(self):
        pass

    def __sendGetRequest(
        self,
        endpoint: str,
        params: dict = None,
        resultsInFile: bool = False,
        fileName: str = None
    ):
        return self.api_tools.get(
            endpoint = endpoint,
            params = params,
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

    def getStatusByStatusGroup(
        self,
        id: int,
        resultsInFile = None,
    ) -> list:
        return self.__sendGetRequest(
            endpoint = self.STATUS_GROUPS_ENDPOINT + '/' + str(id) + '/statuses',
            resultsInFile=resultsInFile,
        )

    def getAllHarmonisedCodes(
        self,
        limit: int,
        offset: int,
        resultsInFile = None,
    ) -> list:
        fileName = None
        if resultsInFile:
            fileName = 'harmonised_codes.xlsx'
        return self.__sendGetRequest(
            endpoint = self.HARMONISED_CODES_ENDPOINT,
            params={
                'limit': limit,
                'offset': offset,
            },
            resultsInFile=resultsInFile,
            fileName=fileName
        )

    def getCurrencies(
        self,
    ) -> list:
        return self.__sendGetRequest(
            endpoint = self.CURRENCIES_ENDPOINT,
        )