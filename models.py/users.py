from database import Base 
from sqlalchemy import Column, String, Integer

class users(Base):
    __tablename__="UserInfo"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)