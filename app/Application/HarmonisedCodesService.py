from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.HarmonisedCodes.HarmonisedCode import HarmonisedCode
from Shared.Domain.Entities.EntityBase import EntityBase
import json


class HarmonisedCodesService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def syncHarmonisedCodes(
        self,
    ) -> list:
        offset = 0
        totalFetched = 0
        totalAvailable = float('inf')

        mock = {
                "paging_info": {
                    "fetched": 2,
                    "limit": 10,
                    "total": 2,
                    "offset": 0
                },
                "data": [
                    {
                        "id": 38366,
                        "code": "01000000",
                        "description": "LIVE ANIMALS"
                    },
                    {
                        "id": 38298,
                        "code": "01010000",
                        "description": "Live horses, asses, mules and hinnies"
                    }
                ]
            }

        while (totalFetched < totalAvailable):
            # receivedHarmonisedCodes = self.repository.getAllHarmonisedCodes(
            #     limit = limit,
            #     offset = offset,
            #     resultsInFile = resultsInFile,
            # )
            harmonisedCodesResponse = mock

            receivedHarmonisedCodes = harmonisedCodesResponse['data']

            for receivedHarmonisedCode in receivedHarmonisedCodes:
                harmonisedCode = HarmonisedCode(
                    id = receivedHarmonisedCode['id'],
                    code = receivedHarmonisedCode['code'],
                    description = receivedHarmonisedCode['description'],
                )
                harmonisedCode.add(harmonisedCode.getModel())

            paginationInfo = harmonisedCodesResponse['paging_info']
            totalFetched += paginationInfo['fetched']
            totalAvailable = paginationInfo['total']
            offset += totalFetched

        EntityBase.commit()

        return json({'message': 'Harmonised codes updated successfully'}), 201