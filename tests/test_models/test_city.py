#!/usr/bin/python3
import unittest
from models.city import City
from models import storage
import pep8
import inspect
from models.base_model import BaseModel
import models
from models import city



class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_functions = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_city_instance(self):
        """Test if City is an instance of the City class"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

        if models.storage_type == 'db':
            self.assertIsNone(city.name)
            self.assertIsNone(city.state_id)
        else:
            self.assertEqual(city.name, "")
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_city_save(self):
        """Test if the save function works for City"""
        self.city.name = "Test City"
        self.city.state_id = "123"
        self.city.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_to_dict(self):
        """Test if the to_dict function works for City"""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_storage(self):
        """Test if City is correctly stored in the storage"""
        storage.new(self.city)
        storage.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_delete(self):
        """Test if the delete function works for City"""
        city_id = self.city.id
        storage.new(self.city)
        storage.save()
        storage.delete(self.city)
        all_cities = storage.all(City)
        city_key = "City." + city_id
        self.assertNotIn(city_key, all_cities)


if __name__ == '__main__':
    unittest.main()
