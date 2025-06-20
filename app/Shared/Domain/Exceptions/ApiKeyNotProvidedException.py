from Shared.Domain.Exceptions.ExceptionBase import ExceptionBase

class ApiNotProvidedException(ExceptionBase):
    def __init__(self):
        super().__init__(
            message = "Bad Request: missing api key",
            code = 400,
        )