from exceptions.exeptions import Data_Exception
from util.connection_db import Connection
from model.user import User
import bcrypt
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
                    user = User()

                    user.name = user_dictionary['name']

                    salt = bcrypt.gensalt()
                    passwd = bytes(user_dictionary['password'], 'utf-8')
                    hashed = bcrypt.hashpw(passwd, salt)
                    user.password = hashed
                    user.save()

                else:
                    raise Data_Exception
            else:
                raise Data_Exception
        else:
            raise Data_Exception
    
    def user_find_by_name(self, user_name):
        
        self.connection.check_connection()
        return json.loads(User.objects(name=user_name).exclude('password').get().to_json())

    def user_list(self, current_page):
        
        items_per_page = 3
        offset = 0

        if current_page > 0:
            offset = current_page * items_per_page

        self.connection.check_connection()
        users_list = User.objects.skip( offset ).exclude('password').limit( items_per_page)
        return json.loads(users_list.to_json())

    def validate_user(self, user):
        if user == None:
            return False
        elif user['name'] == None or user['name'].strip() == "":
            return False
        elif user['password'] == None or user['password'].strip() == "":
            return False
        else:
            return True