from mongoengine import Document, StringField, BinaryField
import json

class User(Document):
    name = StringField()
    email = StringField()
    password = BinaryField()