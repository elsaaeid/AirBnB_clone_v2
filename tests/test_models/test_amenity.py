#!/usr/bin/python3
from datetime import datetime
import inspect
import pep8
import unittest
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel

class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_functions = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(Amenity.__doc__, None, "amenity.py needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1, "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None, "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1, "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_functions:
            self.assertIsNot(func[1].__doc__, None, "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1, "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

import unittest
import models  # Assuming the models module is imported

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""
import unittest
import models  # Assuming the models module is imported

class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test case"""
        cls.place = Place()

    def setUp(self):
        """Set up a variable"""
        self.place = Place(name="Test Place")

    def tearDown(self):
        """Clean up after test cases"""
        del self.place
        storage.delete(self.place)

    def test_place_attributes(self):
        """Test Place attributes"""
        attributes = {
            "city_id": (str, ""),
            "user_id": (str, ""),
            "name": (str, "Test Place"),
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
            self.assertTrue(hasattr(self.place, attr))
            if models.storage_type == 'db':
                self.assertIsNone(getattr(self.place, attr))
            else:
                self.assertEqual(type(getattr(self.place, attr)), attr_type)
                self.assertEqual(getattr(self.place, attr), default_value)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertNotIn('_sa_instance_state', new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn('__class__', new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)
        self.assertEqual(am.created_at.strftime(t_format), new_d["created_at"])
        self.assertEqual(am.updated_at.strftime(t_format), new_d["updated_at"])

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_amenity_instance(self):
        """Test if Amenity is an instance of the Amenity class"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_save(self):
        """Test if the save function works for Amenity"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        """Test if the to_dict function works for Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(self.amenity.__class__.__name__, 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_storage(self):
        """Test if Amenity is correctly stored in the storage"""
        storage.new(self.amenity)
        storage.save()
        all_amenities = storage.all(Amenity)
        amenity_key = "Amenity." + self.amenity.id
        self.assertIn(amenity_key, all_amenities)

    def test_amenity_delete(self):
        """Test if the delete function works for Amenity"""
        amenity_id = self.amenity.id
        storage.new(self.amenity)
        storage.save()
        storage.delete(self.amenity)
        all_amenities = storage.all(Amenity)
        amenity_key = "Amenity." + amenity_id
        self.assertNotIn(amenity_key, all_amenities)


if __name__ == '__main__':
    unittest.main()
