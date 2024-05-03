#!/usr/bin/python3
"""create class DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")


class DBStorage:
    """class DBStorage"""
    classes = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }
    __engine = None
    __session = None

    def __init__(self):
        """initialize instances"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dictionary of instance attributes"""
        new_dict = {}
        if cls:
            if isinstance(cls, str) and cls in self.classes:
                for obj in self.__session.query(self.classes[cls]).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
            elif isinstance(cls, type) and issubclass(cls, BaseModel):
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
        else:
            for cls in self.classes.values():
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the
        current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database
        session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and
        the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()

    def get(self, cls, id):
        """Retrieves an instance based on the class and ID"""
        if cls in self.classes.values() and id and isinstance(id, str):
            d_obj = self.all(cls)
            for key, value in d_obj.items():
                if key.split(".")[1] is id:
                    return value
        return None

    def count(self, cls=None):
        """ counts """
        data = self.all(cls)
        if cls in self.classes.values():
            data = self.all(cls)
        return len(data)
