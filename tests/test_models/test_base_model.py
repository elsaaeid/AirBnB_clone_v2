#!/usr/bin/python3
import unittest
import inspect
import pep8
from datetime import datetime
import os
import models
from models.base_model import BaseModel

module_doc = BaseModel.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests for the documentation
    and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.base_functions = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that base_model.py and test_base_model.py conform to PEP8"""
        files_to_check = ['models/base_model.py',
                          'tests/test_models/test_base_model.py']
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

    def test_module_docstring(self):
        """Test for module docstring in BaseModel"""
        module_doc = inspect.getdoc(BaseModel)
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for class docstring in BaseModel"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstring(self):
        """Test for docstrings in BaseModel methods"""
        for func_name, func in self.base_functions:
            with self.subTest(function=func_name):
                self.assertIsNot(
                    func.__doc__,
                    None,
                    f"{func_name} method needs a docstring"
                )
                self.assertTrue(
                    len(func.__doc__) > 1,
                    f"{func_name} method needs a docstring"
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Initialize a new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """Test if BaseModel is an instance of the BaseModel class"""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_creation(self):
        """Test if BaseModel creates a unique ID"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """Test if created_at is of type datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test if BaseModel has a string representation"""
        string_representation = str(self.model)
        dict_ = self.model.__dict__
        expected_representation = f"[BaseModel] ({self.model.id}) {dict_}"
        self.assertEqual(string_representation, expected_representation)

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_updated_at_save(self):
        """Test function to save updated_at attribute"""
        self.model.save()
        self.assertIsInstance(self.model.updated_at, datetime)

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
        model = BaseModel()
        model_id = model.id  # Get the ID before deletion
        model.delete()
        # Check if the model instance is no longer present in the storage
        self.assertNotIn(model_id, models.storage.all(BaseModel))

    def test_new_instance(self):
        """Test if a new instance of BaseModel is created"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances
        have correct datetime attributes"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertLessEqual(model1.created_at, datetime.utcnow())
        self.assertLessEqual(model2.created_at, datetime.utcnow())
        self.assertEqual(model1.created_at, model1.updated_at)
        self.assertEqual(model2.created_at, model2.updated_at)
        self.assertNotEqual(model1.created_at, model2.created_at)
        self.assertNotEqual(model1.updated_at, model2.updated_at)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary"""
        self.model.name = "Holberton"
        self.model.my_number = 89
        new_dict = self.model.to_dict()
        expected_attributes = ["id", "created_at", "updated_at",
                               "name", "my_number", "__class__"]
        self.assertCountEqual(new_dict.keys(), expected_attributes)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['name'], "Holberton")
        self.assertEqual(new_dict['my_number'], 89)

    def test_to_dict_values(self):
        """Test that values in to_dict are correct"""
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.model.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         self.model.created_at.strftime(format_t))
        self.assertEqual(new_dict["updated_at"],
                         self.model.updated_at.strftime(format_t))


if __name__ == '__main__':
    unittest.main()
