from app import db

class StatusGroupModel(db.Model):
    __tablename__ = 'status_groups'

    id = db.Column(db.Integer, primary_key=True)
    group_key = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    status = db.relationship('StatusModel', back_populates='status_group')

    def toDict(self):
        return {
            'id': self.id,
            'group_key': self.group_key,
            'description': self.description,
            }