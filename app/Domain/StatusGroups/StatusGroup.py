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
        statuses: dict = [],
    ):
        self.id = id
        self.key = key
        self.description = description
        self.statuses = []

        for status in statuses:
            self.addStatus(
                id = status['id'],
                code = status['code'],
                description = status['description'],
                shortDescription = status['shortDescription'],
                statusGroupId = status['statusGroupId'],
            )

        self.model = StatusGroupModel(
            id = self.id,
            group_key = self.key,
            description = self.description,
        )

    def getId(self) -> int:
        return self.id

    def getStatus(self) -> list:
        statusIds = []
        for status in self.statuses:
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
        statusGroupId = int,
    ) -> Self:
        status = Status(
            id,
            code,
            description,
            shortDescription,
            statusGroupId,
        )
        self.statuses.append(status)
        return Self