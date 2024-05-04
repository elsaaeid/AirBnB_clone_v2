import json
import os
from datetime import datetime
import uuid
from hashlib import md5
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models  # Assuming models is a module in your application

# Check the storage type and define the base class accordingly
if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel(Base):
    """Base model that all classes will inherit from"""
    __abstract__ = True

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    password = Column(String(128))

    # Constructor to initialize the base model
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
        if 'password' in kwargs:
            self.password = md5(kwargs['password'].encode()).hexdigest()
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

    # Method to update the instance with the provided attribute dictionary
    def update(self, attribute_dict):
        for key, value in attribute_dict.items():
            setattr(self, key, value)
        self.save()

    # String representation of the instance
    def __str__(self):
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    # Convert instance into dict format
    def to_dict(self, secure_pwd=True):
        new_dict = self.__dict__.copy()
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        dT = datetime
        if "created_at" in new_dict and isinstance(new_dict["created_at"], dT):
            new_dict["created_at"] = new_dict["created_at"].strftime(format_t)
        if "updated_at" in new_dict and isinstance(new_dict["updated_at"], dT):
            new_dict["updated_at"] = new_dict["updated_at"].strftime(format_t)
        new_dict["__class__"] = type(self).__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if secure_pwd and models.storage_type == "db":
            del new_dict['password']
        return new_dict

    # Method to save the instance
    def save(self):
        if models.storage_type != 'db':
            self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    # Method to delete the instance from the storage
    def delete(self):
        models.storage.delete(self)
