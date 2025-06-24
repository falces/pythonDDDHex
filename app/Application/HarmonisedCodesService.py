from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.HarmonisedCodes.HarmonisedCode import HarmonisedCode
from Domain.HarmonisedCodes.HarmonisedCodesModel import HarmonisedCodesModel
from app import db
# import json

class HarmonisedCodesService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def syncHarmonisedCodes(
        self,
    ) -> list:
        limit = 250
        offset = 0
        totalFetched = 0
        totalAvailable = float('inf')

        while (totalFetched < totalAvailable):
            harmonisedCodesResponse = self.repository.getAllHarmonisedCodes(
                limit = limit,
                offset = offset,
            )

            receivedHarmonisedCodes = harmonisedCodesResponse['data']

            for receivedHarmonisedCode in receivedHarmonisedCodes:
                id = receivedHarmonisedCode['id']
                code = receivedHarmonisedCode['code']
                description = receivedHarmonisedCode['description']
                harmonisedCode = HarmonisedCode(
                    id,
                    code,
                    description,
                )
                harmonisedCodeModel = HarmonisedCodesModel(
                    id = harmonisedCode.id,
                    code = harmonisedCode.code,
                    description = harmonisedCode.description
                )
                db.session.add(harmonisedCodeModel)

            paginationInfo = harmonisedCodesResponse['paging_info']
            totalFetched += paginationInfo['fetched']
            totalAvailable = paginationInfo['total']
            offset += totalFetched

            db.session.commit()

        return {'message': 'Harmonised codes updated successfully'}, 201