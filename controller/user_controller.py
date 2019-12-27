from exceptions.exeptions import Data_Exception
from model.user import User
from util.connection_db import Connection
from pymongo.errors import ServerSelectionTimeoutError
import json

class User_Controller():
    def user_save(self, new_user):
        # transform string to string_json
        string_json = json.dumps(eval(new_user))
        # transform string_json to dictionary
        user_dictionary = json.loads(string_json)
        if 'name' in user_dictionary:
            if 'password' in user_dictionary:
                if self.validate_user(user_dictionary):
                    connection = Connection()
                    try:
                        connection.check_connection()
                    except ServerSelectionTimeoutError:
                        print('erro in connection with database')

                    #User(new_user).save()
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
        return [{'nome':'alan'}]
    
    def validate_user(self, user):
        if user == None:
            return False
        elif user['name'] == None or user['name'].strip() == "":
            return False
        elif user['password'] == None or user['password'].strip() == "":
            return False
        else:
            return True