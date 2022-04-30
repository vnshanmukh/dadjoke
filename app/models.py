from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from db import Base

class Joke(Base):
    __tablename__ = "jokes"
    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "jokeusers.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
class User(Base):
    __tablename__ = "jokeusers"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String,nullable= False, unique= True)
    password = Column(String,nullable= False)
    firstname = Column(String,nullable= False)
    lastname = Column(String,nullable= False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))