import mongoengine


class User(mongoengine.Document):
    name = mongoengine.StringField()
    email = mongoengine.StringField()
    password = mongoengine.StringField()