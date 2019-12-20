from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required

class User_Resource(Resource):
    @jwt_required
    def get(self):
        return "200",200
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('user', location='json')

        return ""

        args = parse.parse_args()
        print(args)


