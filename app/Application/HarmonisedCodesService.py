from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.HarmonisedCodes.HarmonisedCode import HarmonisedCode
from Domain.HarmonisedCodes.HarmonisedCodesModel import HarmonisedCodesModel
from flask import current_app


class HarmonisedCodesService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def syncHarmonisedCodes(
        self,
    ) -> list:
        limit = 500
        offset = 5000
        totalFetched = 5000
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
                current_app.db.session.add(harmonisedCodeModel)

            paginationInfo = harmonisedCodesResponse['paging_info']
            totalFetched += paginationInfo['fetched']
            totalAvailable = paginationInfo['total']
            offset += totalFetched

            current_app.db.session.commit()

        return {'message': 'Harmonised codes updated successfully'}, 201