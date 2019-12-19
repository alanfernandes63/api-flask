import time
import os

import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField()
    endereco = mongoengine.StringField()

from flask import Flask

#10.51.67.233
mongoengine.connect('project1',host="mongodb",port=27017)

app = Flask(__name__)

from user_recource import User_Resource
from flask_restful import Api

api = Api(app)

api.add_resource(User_Resource,'/user/')

@app.route('/<string:nome>')
def hello(nome):
    #print(User.objects(name=nome).get()['name'])
    user = User.objects(name=nome).get()
    return {"name":user['name'],"endereco":user["endereco"]}

from flask import request

@app.route('/',methods=['POST'])
def post():
    json = request.get_json()
    user = User()
    user.name = json['name']
    user.endereco = json['endereco']
    user.save()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1028, debug=True)