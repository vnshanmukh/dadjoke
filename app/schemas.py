from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
class Joke(BaseModel):
    content : str
class Joke_out(BaseModel):
    content : str
    class Config:
        orm_mode = True
class Joke_out_id(Joke_out):
    id : int 
    class Config:
        orm_mode = True
class UserCreate(BaseModel):
    firstname : str
    lastname : str
    email : EmailStr
    password : str
class UserOut(BaseModel):
    id : int
    firstname : str
    lastname : str
    email : EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None
    email : Optional[EmailStr] = None