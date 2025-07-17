from Shared.Domain.Exceptions.IncorrectValueException import IncorrectValueException


class IncorrectCountryCodeException(IncorrectValueException):
    def __init__(
        self,
        value: any,
    ):
        super().__init__(
            value = value,
            message = "Incorrect Country Code value: " + str(value),
        )