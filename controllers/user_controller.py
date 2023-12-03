from models.user_model import UserModel
from models.rol_model import RolModel
from db import db
import hashlib

class UserController:

    def create(self, json):
        user = UserModel(
            name=json['name'],
            email=json['email'],
            password=self.__hashPwd(json['password']),
            rol_id=json['rol_id']
        )
        db.session.add(user)
        db.session.commit()
        return user.toJson(), 201
    
    def getAll(self):
        users = UserModel.query.all()
        response = []
        for user in users:
            response.append(user.toJson())
        return response, 200
    
    def __hashPwd(self, password):
        pwdBytes = password.encode('utf-8')
        pwdHashed = hashlib.sha256(pwdBytes).hexdigest()
        return pwdHashed
