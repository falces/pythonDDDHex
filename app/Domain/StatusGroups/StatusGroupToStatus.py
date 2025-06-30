from Domain.StatusGroups.StatusGroupToStatusModel import StatusGroupToStatusModel
from Shared.Domain.Entities.EntityBase import AggregateRootBase


class StatusGroupToStatus(AggregateRootBase):
    def __init__(
        self,
        status_group_id: int,
        status_id: int,
    ):
        self.status_group_id = status_group_id
        self.status_id = status_id
        self.model = StatusGroupToStatusModel(
            status_group_id = self.status_group_id,
            status_id = self.status_id,
        )

    def toDict(self) -> dict:
        return {
            "status_group_id": self.status_group_id,
            "status_id": self.status_id,
            }