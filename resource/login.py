from flask_restplus import Resource
from flask_jwt_extended import create_access_token
from flask import jsonify
import datetime


class Login(Resource):
    def get(self):
        #ret = {'access_token': create_access_token('alan')}
        #return jsonify(ret), 200
        expires = datetime.timedelta(days=365)
        token = create_access_token(identity='alan', expires_delta=expires)
        return token