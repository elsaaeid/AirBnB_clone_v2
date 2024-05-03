#!/usr/bin/python3
"""FileStorage class"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes back to instances
    """
    classes = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary __objects"""
        if cls is not None:
            return {key: value for key,
                    value in self.__objects.items() if isinstance(value, cls)}
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    if class_name in self.classes:
                        self.all()[key] = self.classes[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Retrieves an object based on class and id"""
        if cls in self.classes.values() and isinstance(id, str):
            for obj in self.all(cls).values():
                if obj.id == id:
                    return obj
        return None

    def count(self, cls=None):
        """Counts the number of objects in storage"""
        return len(self.all(cls))
