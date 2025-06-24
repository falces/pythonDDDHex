from Shared.Domain.Entities.EntityBase import EntityBase


class HarmonisedCode(EntityBase):
    def __init__(
        self,
        id: int,
        code: str,
        description: str,
    ):
        self.id = id
        self.code = code
        self.description = description

    def toDict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
        }