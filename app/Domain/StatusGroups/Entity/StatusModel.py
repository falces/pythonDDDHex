from app import db

class StatusModel(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)
    short_description = db.Column(db.String(100), unique=False, nullable=False)
    status_group_id = db.Column(db.Integer, db.ForeignKey('status_groups.id'))
    status_group = db.relationship('StatusGroupModel', back_populates='status')

    def toDict(self):
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'short_description': self.short_description,
            'status_group_id': self.status_group_id,
        }