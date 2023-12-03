from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey, Column
from db import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(Text, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    rol_id = Column(Integer, ForeignKey('rol.id'), nullable=False)

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'status': self.status,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'rol_id': self.rol_id
        }