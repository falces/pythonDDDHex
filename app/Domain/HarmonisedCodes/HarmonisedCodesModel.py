from app import db


class HarmonisedCodesModel(db.Model):
    __tablename__ = 'harmonised_codes'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), unique=True, nullable=False)
    description = db.Column(db.String(256), unique=False, nullable=False)

