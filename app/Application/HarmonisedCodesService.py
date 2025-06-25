from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.HarmonisedCodes.HarmonisedCode import HarmonisedCode
from Domain.HarmonisedCodes.HarmonisedCodesModel import HarmonisedCodesModel
from app import db, app


class GetHarmonisedCodesService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def getAllHarmonisedCodes(
        self,
        resultsInFile: bool = False,
    ) -> list:

        allHarmonisedCodes = HarmonisedCodesModel.query.all()
        harmonisedCodes = []

        app.logger.info("Total harmonised codes retrieved from database: %s", len(allHarmonisedCodes))

        for harmonisedCode in allHarmonisedCodes:
            harmonisedCodes.append(harmonisedCode.toDict())

        return harmonisedCodes

class ImportHarmonisedCodesService:
    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository()

    def syncHarmonisedCodes(
        self,
    ) -> list:
        limit = 500
        offset = 0
        numberOfRequests = 0

        while True:
            numberOfRequests += 1
            app.logger.info("Limit: %s, offset: %s", limit, offset)
            harmonisedCodesResponse = self.repository.getAllHarmonisedCodes(
                limit = limit,
                offset = offset,
            )

            if "data" in harmonisedCodesResponse:
                receivedHarmonisedCodes = harmonisedCodesResponse["data"]
            else:
                receivedHarmonisedCodes = harmonisedCodesResponse

            app.logger.info("Received %s harmonised codes", len(receivedHarmonisedCodes))

            if not receivedHarmonisedCodes:
                app.logger.info("Total requests: %s", numberOfRequests)
                break

            for receivedHarmonisedCode in receivedHarmonisedCodes:
                id = receivedHarmonisedCode['id']
                code = receivedHarmonisedCode['code']
                description = receivedHarmonisedCode['description']
                harmonisedCode = HarmonisedCode(
                    id,
                    code,
                    description,
                )

                db.session.add(harmonisedCode.model)
                db.session.commit()

            offset += limit

        return {'message': 'Harmonised codes updated successfully'}, 201