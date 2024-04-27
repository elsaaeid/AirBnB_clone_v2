#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.model = BaseModel()
        self.model.name = "Test BaseModel"
        self.model.save()

    def tearDown(self):
        """Clean up after test cases"""
        del self.model

    def test_instance_creation(self):
        """Test if BaseModel is an instance of the BaseModel class"""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_creation(self):
        """Test if BaseModel creates a unique ID"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """Test if created_at is of type datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test if to_dict function works for BaseModel"""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_representation(self):
        """Test if BaseModel has a string representation"""
        string_representation = str(self.model)
        self.assertEqual(string_representation, "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__))

    def test_save(self):
        """Test if the save function works for BaseModel"""
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_reload(self):
        """Test if the reload function works for BaseModel"""
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.model.reload()
        self.assertEqual(initial_updated_at, self.model.updated_at)

    def test_attributes(self):
        """Test if BaseModel has the expected attributes"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_save_to_file(self):
        """Test if BaseModel is saved to file"""
        self.model.save()
        file_path = "file.json"
        self.assertTrue(os.path.exists(file_path))

    def test_delete(self):
        """Test if the delete function works for BaseModel"""
        self.model.delete()
        self.assertNotIn(self.model, BaseModel._BaseModel__objects)

    def test_new_instance(self):
        """Test if a new instance of BaseModel is created"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)


if __name__ == '__main__':
    unittest.main()
