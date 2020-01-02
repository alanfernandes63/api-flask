from model.todo import Todo
from util.connection_db import Connection
from controller.user_controller import User_Controller
from model.user import User

class Todo_Controller():

    connection = None

    def __init__(self):
        self.connection = Connection()

    def save(self, todo, user_name):
        user_controller = User_Controller()
        self.connection.check_connection();

        user = User.objects(name=user_name).get()

        

