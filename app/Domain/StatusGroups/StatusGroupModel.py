from app import db
from Domain.StatusGroups.StatusGroupToStatusModel import StatusGroupToStatusModel


class StatusGroupModel(db.Model):
    __tablename__ = 'status_groups'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    group_key = db.Column(
        db.String(100),
        unique=False,
        nullable=False
    )

    description = db.Column(
        db.String(250),
        unique=False,
        nullable=False
    )

    status = db.relationship(
        'StatusModel',
        secondary=StatusGroupToStatusModel.__table__,
        back_populates='status_groups'
    )

    def toDict(self):
        statuses = []
        for status in self.status:
            statuses.append(status.toDict())
        return {
            'id': self.id,
            'group_key': self.group_key,
            'description': self.description,
            'statuses': statuses,
        }