from pydantic import BaseModel


class Model(BaseModel, extra='allow'):
    """Base class for model objects"""