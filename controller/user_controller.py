from exceptions.exeptions import Data_Exception
from model.user import User
from util.connection_db import Connection
import json

class User_Controller():

    connection = None

    def __init__(self):

        self.connection = Connection()

    def user_save(self, new_user):
        # transform string to string_json
        string_json = json.dumps(eval(new_user))
        # transform string_json to dictionary
        user_dictionary = json.loads(string_json)
        if 'name' in user_dictionary:
            if 'password' in user_dictionary:
                if self.validate_user(user_dictionary):
                    
                    self.connection.check_connection()
                    User(new_user).save()

                else:
                    raise Data_Exception
            else:
                raise Data_Exception
        else:
            raise Data_Exception
    
    def user_find_by_id(self, id):

        try:
            #TODO: find user in database
            User.objects(_id=self.id)
            return []

        except:
            return []

    def user_list(self):
        #TODO: list all user from database
        users = []
        for user in User.objects():
            users.append(user['name'])
        #print(users)
        return users
    
    def validate_user(self, user):
        if user == None:
            return False
        elif user['name'] == None or user['name'].strip() == "":
            return False
        elif user['password'] == None or user['password'].strip() == "":
            return False
        else:
            return True