from flask_restplus import Resource,reqparse
from flask_jwt_extended import jwt_required
from controller.user_controller import User_Controller
from exceptions.exeptions import None_User_Exception,User_Not_Found


class My_Exception(Exception):
    """ my_exeption"""
    pass


class User_Resource(Resource):

    @jwt_required
    def get(self):
        return "200",200    

    def post(self):
        user_controller = User_Controller()

        parse = reqparse.RequestParser()
        parse.add_argument('user', location='json')

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


