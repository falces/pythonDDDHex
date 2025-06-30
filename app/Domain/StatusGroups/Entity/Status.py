from Shared.Domain.Entities.EntityBase import EntityBase
from Domain.StatusGroups.Entity.StatusModel import StatusModel


class Status(EntityBase):
    def __init__(
        self,
        id: int,
        code: str,
        description: str,
        shortDescription: str,
        statusGroupId: int,
    ):
        self.id = id
        self.code = code
        self.description = description
        self.shortDescription = shortDescription
        self.statusGroupId = statusGroupId

        self.model = StatusModel(
            id = self.id,
            code = self.code,
            description = self.description,
            short_description = self.shortDescription,
        )

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
            "shortDescription": self.shortDescription,
            "statusGroupId": self.statusGroupId,
        }

    def getId(self) -> int:
        return self.id