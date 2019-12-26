from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from controller.user_controller import User_Controller
from exceptions.exeptions import Data_Exception

class User_Resource_One(Resource):

    #@jwt_required
    @jwt_refresh_token_required
    def get(self):
        parse = parse = reqparse.RequestParser()
        parse.add_argument('id', type=str)
        args = parse.parse_args()

        user_controller = User_Controller()
        user_controller.user_find_by_id(args['id'])

    @jwt_refresh_token_required
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

class User_Resource_List(Resource):
    @jwt_refresh_token_required
    def get(self):
        user_controller = User_Controller()
        return user_controller.user_list()