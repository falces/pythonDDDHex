from app import db
from Domain.StatusGroups.StatusGroupToStatusModel import StatusGroupToStatusModel


class StatusModel(db.Model):
    __tablename__ = 'status'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    code = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )

    description = db.Column(
        db.String(250),
        unique=False,
        nullable=False
    )

    short_description = db.Column(
        db.String(100),
        unique=False,
        nullable=False
    )

    status_groups = db.relationship(
        'StatusGroupModel',
        secondary=StatusGroupToStatusModel.__table__,
        back_populates='status'
    )

    def toDict(self):
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'short_description': self.short_description,
        }