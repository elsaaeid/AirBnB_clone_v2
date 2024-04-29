#!/usr/bin/python3
import unittest
import pep8
import inspect
from models.place import Place
from models import storage
from models.base_model import BaseModel
import models


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_functions = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_equality_place(self):
        """Test that models/place.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")

    def test_pep8_equality_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(models.place.__doc__, None, "place.py needs a docstring")
        self.assertTrue(len(models.place.__doc__) >= 1, "place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None, "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1, "Place class needs a docstring")

    def test_place_func_docstring(self):
        """Test for the presence of docstrings in Place methods"""
        for func_name, func in self.place_functions:
            self.assertIsNot(func.__doc__, None, f"{func_name} method needs a docstring")
            self.assertTrue(len(func.__doc__) >= 1, f"{func_name} method needs a docstring")


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def setUp(self):
        """Set up the test environment"""
        self.place = Place()

    def test_is_subclass_and_attributes(self):
        """Test that Place is a subclass of BaseModel and has attributes"""
        place = self.place
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_instance(self):
        """Test if Place is an instance of the Place class"""
        place = Place()
        self.assertIsInstance(place, Place)

        # Add assertions for attributes and their types

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test_place_save(self):
        """Test if the save function works for Place"""
        self.place.name = "Test Place"
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.save()
        all_places = storage.all(Place)
        place_key = "Place." + self.place.id
        self.assertIn(place_key, all_places)

    def test_place_to_dict(self):
        """Test if the to_dict function works for Place"""
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.__class__.__name__, 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_storage(self):
        """Test if Place is correctly stored in the storage"""
        storage.new(self.place)
        storage.save()
        all_places = storage.all(Place)
        place_key = "Place." + self.place.id
        self.assertIn(place_key, all_places)

    def test_place_delete(self):
        """Test if the delete function works for Place"""
        place_id = self.place.id
        storage.new(self.place)
        storage.save()
        storage.delete(self.place)
        all_places = storage.all(Place)
        place_key = "Place." + place_id
        self.assertNotIn(place_key, all_places)


if __name__ == '__main__':
    unittest.main()