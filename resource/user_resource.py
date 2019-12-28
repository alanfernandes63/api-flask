from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from controller.user_controller import User_Controller
from exceptions.exeptions import Data_Exception
from pymongo.errors import ServerSelectionTimeoutError
from mongoengine.queryset import DoesNotExist

class User_Resource_One(Resource):

    #@jwt_required
    @jwt_refresh_token_required
    def get(self):
        parse = parse = reqparse.RequestParser()
        parse.add_argument('name', type=str)
        args = parse.parse_args()

        user_controller = User_Controller()
        try:
            user = user_controller.user_find_by_name(args['name'])
            return user
        except DoesNotExist:
            return "user not found", 404

    #@jwt_refresh_token_required
    def post(self):
        user_controller = User_Controller()

        parse = reqparse.RequestParser()
        parse.add_argument('user', required=True, location='json', help="user is required!")

        args = parse.parse_args()

        try:

            user_controller.user_save(args['user'])
            return "user created", 201

        except Data_Exception:
            return "error in data", 400
        except ServerSelectionTimeoutError:
            print("error in connection with database")
            return "servico temporariamente indiponível", 503

class User_Resource_List(Resource):
    #@jwt_refresh_token_required
    def get(self):
        user_controller = User_Controller()
        return user_controller.user_list()