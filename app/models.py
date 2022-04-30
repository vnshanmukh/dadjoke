from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, false
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from db import Base

class Joke(Base):
    __tablename__ = "Jokes"
    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))