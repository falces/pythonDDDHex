class Country:
    def __init__(
        self,
        id: int,
        name: str,
        code: str,
        hasSubzone: bool = False,
        isEUMember: bool = False,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.hasSubzone = hasSubzone
        self.isEUMember = isEUMember
        
    def toDict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "hasSubzone": self.hasSubzone,
            "isEUMember": self.isEUMember,
        }