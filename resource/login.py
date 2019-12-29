from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restplus import Resource,reqparse
from flask_restplus import Resource
from flask import jsonify
import datetime
import json


class Login(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('user', required=True, location='json', help="user is required!")

        args = parse.parse_args()
        user_json = json.dumps(eval(args['user']))

        user_dictionary = json.loads(user_json)
        username = user_dictionary['username']
        password = user_dictionary['password']

        #ret = {'access_token': create_access_token('alan')}
        #return jsonify(ret), 200
        #expires = datetime.timedelta(days=1)
        #token = create_access_token(identity='alan', expires_delta=expires)
        #token = create_refresh_token(identity='alan', expires_delta=expires)
        #return token
        return ""