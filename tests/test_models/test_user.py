#!/usr/bin/python3
import unittest
import inspect
import models
from datetime import datetime
from models import user
from models.base_model import BaseModel
import pep8
from models import storage
from models.user import User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_functions = inspect.getmembers(user.User, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that user.py and test_user.py conform to PEP8"""
        files_to_check = ['models/user.py',
                          'tests/test_models/test_user.py']
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

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(
            user.__doc__,
            None,
            "user.py needs a docstring"
        )
        self.assertTrue(
            len(user.__doc__) >= 1,
            "user.py needs a docstring"
        )

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(
            user.User.__doc__,
            None,
            "User class needs a docstring"
        )
        self.assertTrue(
            len(user.User.__doc__) >= 1,
            "User class needs a docstring"
        )

    def test_user_func_docstring(self):
        """Test for the presence of docstrings in User methods"""
        for func_name, func in self.user_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.user = User()

    def test_user_attributes(self):
        """Test User attributes"""
        user = self.user
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

        if models.storage_type == 'db':
            self.assertIsNone(user.email)
            self.assertIsNone(user.password)
            self.assertIsNone(user.first_name)
            self.assertIsNone(user.last_name)
        else:
            self.assertEqual(user.email, "")
            self.assertEqual(user.password, "")
            self.assertEqual(user.first_name, "")
            self.assertEqual(user.last_name, "")

    def test_user_save(self):
        """Test if the save function works for User"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()
        all_users = storage.all(User)
        user_key = "User." + self.user.id
        self.assertIn(user_key, all_users)

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_updated_at_save(self):
        """Test function to save updated_at attribute"""
        self.user.save()
        actual = type(self.user.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """test to_dict method creates a dictionary"""
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in user.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values to_dict are correct"""
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         user.created_at.strftime(format_t))
        self.assertEqual(new_dict["updated_at"],
                         user.updated_at.strftime(format_t))

    def test_user_storage(self):
        """Test if User is correctly stored in the storage"""
        storage.new(self.user)
        storage.save()
        all_users = storage.all(User)
        user_key = "User." + self.user.id
        self.assertIn(user_key, all_users)

    def test_user_delete(self):
        """Test if the delete function works for User"""
        user_id = self.user.id
        storage.new(self.user)
        storage.save()
        storage.delete(self.user)
        all_users = storage.all(User)
        user_key = "User." + user_id
        self.assertNotIn(user_key, all_users)


if __name__ == '__main__':
    unittest.main()
