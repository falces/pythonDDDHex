from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.StatusGroups.StatusGroup import StatusGroup
from Domain.StatusGroups.Entity.Status import Status
from Domain.StatusGroups.StatusGroupToStatus import StatusGroupToStatus
from Domain.StatusGroups.StatusGroupToStatusModel import StatusGroupToStatusModel
from Domain.StatusGroups.Entity.StatusModel import StatusModel
from app import db
from Domain.StatusGroups.StatusGroupModel import StatusGroupModel


class StatusGroupRepository(AbstractRepository):
    def __init__(self):
        self.model = StatusGroupModel()

    def save(
        self,
        StatusGroup: StatusGroup,
    ):
        db.session.add(StatusGroup.getModel())
        for status in StatusGroup.statuses:
            if not self.findStatusById(status.id):
                db.session.add(status.getModel())

            statusGroupToStatus = StatusGroupToStatus(
                status_group_id = StatusGroup.id,
                status_id = status.id,
            )

            if not self.findRelation(statusGroupToStatus, StatusGroup.id, status.id):
                db.session.add(statusGroupToStatus.model)
        db.session.commit()

    def findAll(
        self,
    ) -> list:
        return self.model.query.all()

    def findStatusById(
        self,
        id: int,
    ) -> StatusGroup:
        return StatusModel.query.filter_by(id=id).first()

    def findRelation(
        self,
        statusGroupToStatus: StatusGroupToStatus,
        statusGroupId: int,
        statusId: int,
    ) -> StatusGroupToStatus:
        return statusGroupToStatus.getModel().query.filter_by(status_group_id=statusGroupId, status_id=statusId).first()

    def findStatusesIdsByStatusGroupId(
        self,
        statusGroupId: int,
    ) -> list:
        return StatusGroupToStatusModel.query.filter_by(
            status_group_id = statusGroupId
        ).all()