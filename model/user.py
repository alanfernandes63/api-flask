from mongoengine import Document, StringField
import json

class User(Document):
    name = StringField()
    email = StringField()
    password = StringField()