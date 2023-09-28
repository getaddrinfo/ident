from pydantic import BaseModel, ConfigDict

class Strict(BaseModel):
    model_config = ConfigDict(extra='forbid')

class Lax(BaseModel):
    model_config = ConfigDict(extra='ignore')