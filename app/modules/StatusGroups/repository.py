from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from modules.StatusGroups.entities import StatusGroup, StatusGroupModel
from .entities import StatusGroupToStatus, StatusGroupToStatusModel, StatusModel
from app import db


class StatusGroupRepository(AbstractRepository):
    def __init__(self):
        self.model = StatusGroupModel()

    def save(
        self,
        StatusGroup: StatusGroup,
    ):
        db.session.add(StatusGroup.getModel())
        for status in StatusGroup.statuses:
            if not self.findById(status.id):
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

    def findById(
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