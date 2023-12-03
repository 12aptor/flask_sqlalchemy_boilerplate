from sqlalchemy import Integer, String, Column, Boolean
from db import db

class RolModel(db.Model):
    __tablename__ = 'rol'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    status = Column(Boolean, nullable=False)