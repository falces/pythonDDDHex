from Shared.Domain.Repositories.AbstractRepository import AbstractRepository


class HarmonisedCodesRepository(AbstractRepository):
    def __init__(self):
        pass

    def findAll(self) -> list:
        return super().findAll()