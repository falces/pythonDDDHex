from Shared.Domain.Models.ModelBase import Model
from app import db

class EntityBase(Model):
    """Base class for domain entitie objects."""

    def __str__(self):
        return f'{type(self).__name__}'

    def __repr__(self):
        return self.__str__()

    def add(
        self,
        model: Model,
    ):
        db.session.add(model)

    def getModel(self):
        return self.model

    @staticmethod
    def commit():
        db.session.commit()

class AggregateRoot(EntityBase):
    """Base class for domain aggregate objects. Consits of 1+ entities"""