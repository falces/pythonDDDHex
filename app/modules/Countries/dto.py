class CountryDTO:
    def __init__(
        self,
        id: int,
        name: int,
        code: str,
        hasSubzone: bool = False,
        isEUMember: bool = False,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.hasSubzone = hasSubzone
        self.isEUMember = isEUMember
