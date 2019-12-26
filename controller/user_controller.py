from exceptions.exeptions import Data_Exception
from model.user import User
import json

class User_Controller():
    def user_save(self, new_user):
        # transform string to string_json
        string_json = json.dumps(eval(new_user))
        # transform string_json to dictionary
        dictionary = json.loads(string_json)
        if 'name' in dictionary:
            # verify if 
            if 'password' in dictionary:
                self.validate_user(dictionary)
            else:
                raise Data_Exception
            print("salvou!")
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
        elif user['name'] == None:
            return False
        elif user['password'] == None:
            return False
        else:
            return True