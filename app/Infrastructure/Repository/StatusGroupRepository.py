from Shared.Domain.Repositories.AbstractRepository import AbstractRepository
from Domain.StatusGroups.StatusGroup import StatusGroup
from Domain.StatusGroups.Entity.Status import Status
from Domain.StatusGroups.StatusGroupToStatus import StatusGroupToStatus
from app import db

class StatusGroupRepository(AbstractRepository):

    def save(
        self,
        StatusGroup: StatusGroup,
    ):
        db.session.add(StatusGroup.getModel())
        for status in StatusGroup.statuses:
            if not self.findById(status, status.id):
                db.session.add(status.getModel())

            statusGroupToStatus = StatusGroupToStatus(
                status_group_id = StatusGroup.id,
                status_id = status.id,
            )

            if not self.findRelation(statusGroupToStatus, StatusGroup.id, status.id):
                db.session.add(statusGroupToStatus.model)
        db.session.commit()

    def findById(
        self,
        status: Status,
        id: int,
    ) -> StatusGroup:
        return status.model.query.filter_by(id=id).first()

    def findRelation(
        self,
        statusGroupToStatus: StatusGroupToStatus,
        statusGroupId: int,
        statusId: int,
    ) -> StatusGroupToStatus:
        return statusGroupToStatus.getModel().query.filter_by(status_group_id=statusGroupId, status_id=statusId).first()