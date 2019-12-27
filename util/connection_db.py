from pymongo import MongoClient

class Connection():
    def check_connection(self):
        client = MongoClient(host='localhost', serverSelectionTimeoutMS=10)
        client.server_info()
        client.close()