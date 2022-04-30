from pydantic import BaseModel
from datetime import datetime
class Joke(BaseModel):
    id : int
    content : str
    created_at : datetime
class Joke_out(BaseModel):
    id : int
    content : str
    class Config:
        orm_mode = True