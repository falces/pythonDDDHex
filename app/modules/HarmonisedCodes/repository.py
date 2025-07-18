from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from modules.HarmonisedCodes.entities import HarmonisedCodesModel



class HarmonisedCodesRepository(AbstractRepository):
    def __init__(self):
        self.model = HarmonisedCodesModel()

    def findAll(self) -> list:
        return super().findAll()

    def findById(
        self,
        id: int
    ) -> HarmonisedCodesModel:
        return super().findById(id)

    def save(
        self,
        model: HarmonisedCodesModel
    ) -> HarmonisedCodesModel:
        pass