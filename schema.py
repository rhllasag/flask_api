
from datetime import datetime
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Department(db.Document):
    meta = {'collection': 'department'}
    name = db.StringField()


class Role(db.Document):
    meta = {'collection': 'role'}
    name = db.StringField()


class Employee(db.Document):
    meta = {'collection': 'employee'}
    name = db.StringField()
    hired_on = db.DateTimeField(default=datetime.now)
    department = db.ReferenceField(Department)
    role = db.ReferenceField(Role)
    
