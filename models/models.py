from sqlalchemy import Column, String, Integer
from db.database import Base

class Item(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    city_code = Column(String)
    status = Column(String)