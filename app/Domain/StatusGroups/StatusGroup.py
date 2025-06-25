from typing import Self
from Domain.StatusGroups.Entity.Status import Status
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

    def getId(self) -> int:
        return self.id

    def getStatus(self) -> list:
        statusIds = []
        for status in self.status:
            statusIds.append(status.getId())
        return statusIds

    def toDict(self) -> dict:
        statusGroup = {
            "id": self.id,
            "key": self.key,
            "description": self.description,
            "status": [],
        }
        for status in self.status:
            statusGroup['status'].append(status.toDict())
        return statusGroup

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