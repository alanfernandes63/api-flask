from pymongo import MongoClient

class Connection():
    def check_connection(self):
        client = MongoClient(host='localhost', serverSelectionTimeoutMS=100)
        client.server_info()
        client.close()