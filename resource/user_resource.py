from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from controller.user_controller import User_Controller
from exceptions.exeptions import None_User_Exception,User_Not_Found

class User_Resource_One(Resource):

    #@jwt_required
    @jwt_refresh_token_required
    def get(self):
        parse = parse = reqparse.RequestParser()
        parse.add_argument('id', type=str)
        args = parse.parse_args()

        user_controller = User_Controller()
        user_controller.user_find_by_id(args['id'])
        print("teste")
        
    def post(self):
        user_controller = User_Controller()

        parse = reqparse.RequestParser()
        parse.add_argument('user', required=True, location='json', help="user is required!")

        args = parse.parse_args()

        try:

            user_controller.save_user(args['user'])
            return "user created", 201

        except None_User_Exception:
            return "no user", 400

class User_Resource_List(Resource):
    
    def get(self):
        user_controller = User_Controller()
        return user_controller.user_list()