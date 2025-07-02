class StatusGroupDTO:
    def __init__(
        self,
        id: int,
        key: str,
        description: str,
        statuses: list,
    ):
        self.id = id
        self.key = key
        self.description = description
        self.statuses = statuses