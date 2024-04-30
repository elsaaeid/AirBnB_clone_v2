#!/usr/bin/python3
import unittest
import pep8
from datetime import datetime
import inspect
from models.city import City
from models import storage
from models.base_model import BaseModel
import models


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_functions = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that city.py and test_city.py conform to PEP8"""
        files_to_check = ['models/city.py',
                          'tests/test_models/test_city.py']
        style_guide = pep8.StyleGuide()
        total_errors = 0
        error_messages = []

        for file_path in files_to_check:
            with self.subTest(path=file_path):
                result = style_guide.check_files([file_path])
                errors = result.total_errors

                if errors > 0:
                    print(f"PEP8 errors in {file_path}:")
                    for error in result.messages:
                        error_messages.append(f"- {error}")
                total_errors += errors
        if total_errors > 0:
            error_message = f"Total PEP8 errors: {total_errors}\n"
            error_message += "\n".join(error_messages)
            self.fail(error_message)

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(models.city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(models.city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(
            City.__doc__,
            None,
            "City class needs a docstring"
        )
        self.assertTrue(
            len(City.__doc__) >= 1,
            "City class needs a docstring"
        )

    def test_city_func_docstring(self):
        """Test for the presence of docstrings in City methods"""
        for func_name, func in self.city_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.city = City()

    def test_is_subclass_and_attributes(self):
        """Test that Place is a subclass of BaseModel and has attributes"""
        city = self.city
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_to_dict(self):
        """test to_dict method creates a dictionary"""
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertNotIn('_sa_instance_state', new_dict)
        for attr in city.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_dict)
        self.assertIn('__class__', new_dict)

    def test_to_dict_values(self):
        """test that values in to_dict are correct"""
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertEqual(city.created_at.strftime(format_t),
                         new_dict["created_at"])
        self.assertEqual(city.updated_at.strftime(format_t),
                         new_dict["updated_at"])

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_city_instance(self):
        """Test if City is an instance of the City class"""
        self.assertIsInstance(self.city, City)

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_city_save(self):
        """Test if the save function works for City"""
        self.city.save()
        actual = type(self.city.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

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
