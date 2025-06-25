from app import db


class HarmonisedCodesModel(db.Model):
    __tablename__ = 'harmonised_codes'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
        }

