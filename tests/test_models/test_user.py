#!/usr/bin/python3
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.user = User()

    def tearDown(self):
        """Clean up after test cases"""
        del self.user

    def test_user_instance(self):
        """Test if User is an instance of the User class"""
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

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

    def test_user_to_dict(self):
        """Test if the to_dict function works for User"""
        user_dict = self.user.to_dict()
        self.assertEqual(self.user.__class__.__name__, 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

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
