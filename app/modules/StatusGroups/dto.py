from Shared.Application.DTOBase import DTOBase


class StatusGroupDTO(DTOBase):
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

class StatusDTO(DTOBase):
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