from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required
from controller.user_controller import User_Controller
from exceptions.exeptions import None_User_Exception,User_Not_Found

class User_Resource_One(Resource):

    #@jwt_required
    def get(self):
        parse = parse = reqparse.RequestParser()
        parse.add_argument('id', type=int)
        args = parse.parse_args()

        #TODO: find user in database

        print(args)

    def post(self):
        user_controller = User_Controller()

        parse = reqparse.RequestParser()
        parse.add_argument('user', required=True, location='json', help="user is required!")

        args = parse.parse_args()
        print(args["user"])

        try:
            user_controller.save_user(args['user'])
            return "user created", 201
        except None_User_Exception:
            return "no user", 400
        except User_Not_Found:
            return "user not found", 404

        return "ok",200

class User_Resource_List(Resource):
    def get(self):
        user_controller = User_Controller()
        return user_controller.user_list()

