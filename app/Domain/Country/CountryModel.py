from app import db


class CountryModel(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    hasSubzone = db.Column(db.Boolean, unique=False, nullable=False)
    isEUMember = db.Column(db.Boolean, unique=False, nullable=False)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "hasSubzone": self.hasSubzone,
            "isEUMember": self.isEUMember,
        }