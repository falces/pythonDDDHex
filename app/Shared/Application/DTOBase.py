class DTOBase:
    def toDict(self) -> dict:
        return vars(self)