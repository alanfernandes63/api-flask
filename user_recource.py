from flask_restful import Resource,reqparse


class User_Resource(Resource):
    parse = None

    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('user', location='json')

    def get(self):
        return "Hello word"
    def post(self):

        args = self.parse.parse_args()
        print(args)


