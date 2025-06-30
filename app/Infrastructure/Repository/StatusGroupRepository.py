from Shared.Domain.Repositories.AbstractEntityRepository import AbstractEntityRepository
from Domain.StatusGroups.StatusGroup import StatusGroup
from app import db

class StatusGroupRepository(AbstractEntityRepository):
    def save(
        self,
        StatusGroup: StatusGroup,
    ):
        db.session.add(StatusGroup.getModel())
        for status in StatusGroup.statuses:
            db.session.add(status.getModel())
        db.session.commit()
