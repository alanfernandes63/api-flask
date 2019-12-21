
from exceptions.exeptions import None_User_Exception,User_Not_Found

class User_Controller():

    def save_user(self, user):
        self.validate_user(user)

    def validate_user(self, user):
        if user == None:
            raise None_User_Exception("User None")
        elif True:
            raise User_Not_Found("User not found")
