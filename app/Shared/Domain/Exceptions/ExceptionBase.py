class ExceptionBase(Exception):
    def __init__(
        self,
        message: str,
        code: int
    ):
        super().__init__(self.MESSAGE + message)
        self.code = code
        
    def getCode(self) -> int:
        return self.code