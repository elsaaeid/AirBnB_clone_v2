#!/usr/bin/python3
import inspect
import pep8
import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_functions = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that amenity.py and test_amenity.py conform to PEP8"""
        files_to_check = ['models/amenity.py',
                          'tests/test_models/test_amenity.py']
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

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(
            Amenity.__doc__,
            None,
            "amenity.py needs a docstring"
        )
        self.assertTrue(
            len(Amenity.__doc__) >= 1,
            "amenity.py needs a docstring"
        )

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(
            Amenity.__doc__,
            None,
            "Amenity class needs a docstring"
        )
        self.assertTrue(
            len(Amenity.__doc__) >= 1,
            "Amenity class needs a docstring"
        )

    def test_amenity_func_docstring(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func_name, func in self.amenity_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.amenity = Amenity()

    def test_is_subclass_and_attributes(self):
        """Test that Place is a subclass of BaseModel and has attributes"""
        amenity = self.amenity
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_to_dict(self):
        """test to_dict method creates a dictionary"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertNotIn('_sa_instance_state', new_dict)
        for attr in amenity.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_dict)
        self.assertIn('__class__', new_dict)

    def test_to_dict_values(self):
        """test that values in to_dict are correct"""
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertEqual(amenity.created_at.strftime(format_t),
                         new_dict["created_at"])
        self.assertEqual(amenity.updated_at.strftime(format_t),
                         new_dict["updated_at"])

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
        self.amenity.save()
        actual = type(self.amenity.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

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
