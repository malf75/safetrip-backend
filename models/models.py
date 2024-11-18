from sqlalchemy import Column, String, Integer
from db.database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class Item(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    city_code = Column(String)
    status = Column(String)