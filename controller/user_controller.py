
from exceptions.exeptions import None_User_Exception,User_Not_Found

class User_Controller():

    def use_save(self, user):
        self.validate_user(user)

    def user_find_by_id(self, id):
        #TODO: find database user
        return

    def user_list(self):
        #TODO: list all user from database
        return [{'nome':'alan'}]

    def validate_user(self, user):
        if user == None:
            raise None_User_Exception("User None")
        elif True:
            raise User_Not_Found("User not found")
