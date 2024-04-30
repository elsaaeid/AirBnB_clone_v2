#!/usr/bin/python3
import unittest
import pep8
import inspect
from datetime import datetime
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

    def test_pep8_equality(self):
        """Test that place.py and test_place.py conform to PEP8"""
        files_to_check = ['models/place.py',
                          'tests/test_models/test_place.py']
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

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(
            models.place.__doc__, None,
            "place.py needs a docstring"
        )
        self.assertTrue(
            len(models.place.__doc__) >= 1,
            "place.py needs a docstring"
        )

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(
            Place.__doc__, None,
            "Place class needs a docstring"
        )
        self.assertTrue(
            len(Place.__doc__) >= 1,
            "Place class needs a docstring"
        )

    def test_place_func_docstring(self):
        """Test for the presence of docstrings in Place methods"""
        for func_name, func in self.place_functions:
            self.assertIsNot(
                func.__doc__, None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def setUp(self):
        """Set up the test environment"""
        self.place = Place()

    def test_is_subclass_and_attributes(self):
        """Test that Place is a subclass of
        BaseModel and has attributes
        """
        place = self.place
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_attributes(self):
        """Test Place attributes"""
        place = Place()
        attributes = {
            "city_id": (str, ""),
            "user_id": (str, ""),
            "name": (str, ""),
            "description": (str, ""),
            "number_rooms": (int, 0),
            "number_bathrooms": (int, 0),
            "max_guest": (int, 0),
            "price_by_night": (int, 0),
            "latitude": (float, 0.0),
            "longitude": (float, 0.0),
            "amenity_ids": (list, []),
        }

        for attr, (attr_type, default_value) in attributes.items():
            self.assertTrue(hasattr(place, attr))
            attr_value = getattr(place, attr)
            if models.storage_type == 'db':
                self.assertEqual(attr_value, None)
            else:
                self.assertEqual(type(attr_value), attr_type)
                self.assertEqual(attr_value, default_value)

    def test_place_instance(self):
        """Test if Place is an instance of the Place class"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_to_dict(self):
        """Test to_dict method creates a dictionary"""
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in place.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in to_dict are correct
        """
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_dict = p.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         p.created_at.strftime(format_t))
        self.assertEqual(new_dict["updated_at"],
                         p.updated_at.strftime(format_t))

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

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_updated_at_save(self):
        """Test function to save updated_at attribute"""
        self.place.save()
        actual = type(self.place.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

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
