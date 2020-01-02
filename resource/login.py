from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restplus import Resource,reqparse
from mongoengine.errors import DoesNotExist
from flask_restplus import Resource
from model.user import User
from flask import jsonify
import datetime
import bcrypt
import json


class Login(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('user', required=True, location='json', help="user is required!")

        args = parse.parse_args()
        user_json = json.dumps(eval(args['user']))

        user_dictionary = json.loads(user_json)
        if 'username' in user_dictionary and 'password' in user_dictionary:
            username = user_dictionary['username']
            password = user_dictionary['password']

            try:
                user = User.objects(name=username).get()
            except DoesNotExist:
                return "user not found", 404

            # checks if the password coming from the request is the same as the one in the database
            if bcrypt.checkpw(bytes(password,'utf-8'), user['password']):
                expires = datetime.timedelta(days=360)
                token = create_refresh_token(identity=username, expires_delta=expires)
                return token, 200
            else:
                return "senha incorreta", 404
        else:
            return "invalid payload", 400