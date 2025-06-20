class Status:
    def __init__(
        self,
        id: int,
        code: str,
        description: str,
        shortDescription: str,
    ):
        self.id = id
        self.code = code
        self.description = description
        self.shortDescription = shortDescription
        
    def toDict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
            "shortDescription": self.shortDescription
        }
    
    def getId(self) -> int:
        return self.id