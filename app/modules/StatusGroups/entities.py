from typing import Self
from Shared.Domain.Entities.EntityBase import AggregateRootBase, EntityBase
from app import db


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

class StatusGroupModel(db.Model):
    __tablename__ = 'status_groups'

    id = db.Column(db.Integer, primary_key=True)
    group_key = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)

    status = db.relationship(
        'StatusModel',
        secondary = 'status_groups_to_status',
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

class Status(EntityBase):
    def __init__(
        self,
        id: int,
        code: str,
        description: str,
        shortDescription: str,
        statusGroupId: int,
    ):
        self.id = id
        self.code = code
        self.description = description
        self.shortDescription = shortDescription
        self.statusGroupId = statusGroupId

        self.model = StatusModel(
            id = self.id,
            code = self.code,
            description = self.description,
            short_description = self.shortDescription,
        )

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
            "shortDescription": self.shortDescription,
            "statusGroupId": self.statusGroupId,
        }

    def getId(self) -> int:
        return self.id

class StatusModel(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20), unique = False, nullable = False)
    description = db.Column(db.String(250), unique = False, nullable = False)
    short_description = db.Column(db.String(100), unique = False, nullable = False)

    status_groups = db.relationship(
        'StatusGroupModel',
        secondary = 'status_groups_to_status',
        back_populates='status'
    )

    def toDict(self):
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'short_description': self.short_description,
        }

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

class StatusGroupToStatusModel(db.Model):
    __tablename__ = 'status_groups_to_status'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    status_group_id = db.Column(db.Integer, db.ForeignKey('status_groups.id'), unique=False, primary_key=False, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), unique=False, primary_key=False, nullable=False)

    def toDict(self) -> dict:
        return {
            "status_group_id": self.status_group_id,
            "status_id": self.status_id,
            }