class EntityBase():
    def getModel(self):
        return self.model

    def toDict(self) -> dict:
        return self.getModel().toDict()

class AggregateRootBase(EntityBase):
    pass