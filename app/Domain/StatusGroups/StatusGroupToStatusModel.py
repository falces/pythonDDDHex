from app import db

class StatusGroupToStatusModel(db.Model):
    __tablename__ = 'status_groups_to_status'

    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )

    status_group_id = db.Column(
        db.Integer,
        db.ForeignKey('status_groups.id'),
        unique=False,
        primary_key=False,
        nullable=False
    )

    status_id = db.Column(
        db.Integer,
        db.ForeignKey('status.id'),
        unique=False,
        primary_key=False,
        nullable=False
    )