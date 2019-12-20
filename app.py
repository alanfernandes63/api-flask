import time
import os

import mongoengine
from flask_restplus import Api
from flask import Flask
from resource.user_resource import User_Resource
from controller.user_controller import User_Controller
from flask import request
from flask_jwt_extended import JWTManager
from resource.login import Login

class User(mongoengine.Document):
    name = mongoengine.StringField()
    endereco = mongoengine.StringField()

#10.51.67.233
mongoengine.connect('project1',host="mongodb",port=27017)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

api = Api(app)
jwt._set_error_handler_callbacks(api)

api.add_resource(User_Resource,'/user/')
api.add_resource(Login,'/login')

@app.route('/<string:nome>')
def hello(nome):
    
    #print(User.objects(name=nome).get()['name'])
    user = User.objects(name=nome).get()
    return {"name":user['name'],"endereco":user["endereco"]}

@app.route('/',methods=['POST'])
def post():
    json = request.get_json()
    print(request.get_json())
    #user = User()
    #user.name = json['name']
    #user.endereco = json['endereco']
    #user.save()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1028)
    #app.run(host='0.0.0.0',port=1028, debug=True)