from mongoengine import Document, LazyReferenceField, StringField

class Todo(Document):
    description = StringField()
    user = LazyReferenceField()
    