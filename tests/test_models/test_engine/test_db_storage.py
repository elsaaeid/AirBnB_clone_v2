#!/usr/bin/python3
import unittest
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pep8
from models.base_model import BaseModel

DBStorage = db_storage.DBStorage
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that db_storage.py to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test  test_db_storage.py to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for docstrings in DBStorage methods"""
        for func in self.dbs_functions:
            self.assertIsNot(func[1].__doc__, None,
                             f"{func[0]} method needs a docstring")
            self.assertTrue(len(func[1].__doc__) >= 1,
                            f"{func[0]} method needs a docstring")


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        all_instances = models.storage_type.all()
        self.assertIsInstance(all_instances, dict)
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        all_instances = models.storage_type.all()
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_new(self):
        """Test that new adds an object to the database"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        all_instances = models.storage_type.all()
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to the db"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        file_path = models.storage_type._DBStorage__engine.file_path
        with open(file_path, 'r') as file:
            data = file.read()
            self.assertIn(new_instance.__class__.__name__ + '.' + new_instance.id, data)

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_get(self):
        """Test that get retrieves an item in db properly"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        retrieved_instance = models.storage_type.get(BaseModel, new_instance.id)
        self.assertEqual(retrieved_instance, new_instance)

    @unittest.skipIf(models.storage_type != 'db', "not testing db storage")
    def test_count(self):
        """Test that count returns the right number of elements in the db"""
        initial_count = len(models.storage_type.all())
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        updated_count = len(models.storage_type.all())
        self.assertEqual(updated_count, initial_count + 1)
