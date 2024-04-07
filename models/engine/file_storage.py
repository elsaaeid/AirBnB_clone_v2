#!/usr/bin/python3
""" FileStorage class """

from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..place import Place
from ..amenity import Amenity
from ..review import Review
import json
import os


class FileStorage:
    """ class to process and convert classes to json file"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ initializes objects """
        pass

    def all(self):
        """ returns all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Creates a new instance """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ Serializes instances """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict.update({key: value.to_dict()})
        json_file = json.dumps(my_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def reload(self):
        """ deserializes instances """
        my_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                json_file = json.loads(my_file.read())
                for key in json_file:
                    FileStorage.__objects[key] = my_dict[json_file[key]
                            ['__class__']](**json_file[key])
        except:
            pass
