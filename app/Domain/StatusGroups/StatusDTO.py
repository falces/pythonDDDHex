class StatusDTO:
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

    def toDict(self) -> dict:
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'shortDescription': self.shortDescription,
            'statusGroupId': self.statusGroupId,
        }