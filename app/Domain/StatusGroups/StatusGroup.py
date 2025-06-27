from typing import Self
from Domain.StatusGroups.Entity.Status import Status
from Domain.StatusGroups.StatusGroupModel import StatusGroupModel
from Shared.Domain.Entities.EntityBase import AggregateRootBase


class StatusGroup(AggregateRootBase):
    def __init__(
        self,
        id: int,
        key: str,
        description: str,
        status: dict = [],
    ):
        self.id = id
        self.key = key
        self.description = description
        self.status = status

        self.model = StatusGroupModel(
            id = self.id,
            group_key = self.key,
            description = self.description,
        )

    def getId(self) -> int:
        return self.id

    def getStatus(self) -> list:
        statusIds = []
        for status in self.status:
            statusIds.append(status.getId())
        return statusIds

    def toDict(self) -> dict:
        return self.model.toDict()

    def addStatus(
        self,
        id: int,
        code: str,
        description: str,
        shortDescription: str,
    ) -> Self:
        status = Status(
            id,
            code,
            description,
            shortDescription,
        )
        self.status.append(status)
        return Self