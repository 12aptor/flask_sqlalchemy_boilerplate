from flask import Flask, request
from db import db
from flask_migrate import Migrate
from controllers.user_controller import UserController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/flask_api_rest'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Mi API REST con Flask funciona! 😎'

@app.route('/users/create', methods=['POST'])
def create_user():
    json = request.get_json()
    controller = UserController()
    return controller.create(json)

@app.route('/users/all')
def get_all_users():
    controller = UserController()
    return controller.getAll()

if __name__ == '__main__':
    app.run(debug=True)