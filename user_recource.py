from flask_restful import Resource

class User_Resource(Resource):
    def get(self):
        return "Hello word"


