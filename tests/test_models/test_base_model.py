#!/usr/bin/python3
import unittest
import inspect
import pycodestyle
import time
from datetime import datetime
import os
import models
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__



class TestBaseModelDocs(unittest.TestCase):
    """Tests for the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.base_functions = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that base_model.py and test_base_model.py conform to PEP8"""
        for path in ['models/base_model.py', 'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring in BaseModel"""
        module_doc = inspect.getdoc(BaseModel)
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for class docstring in BaseModel"""
        self.assertIsNot(BaseModel.__doc__, None, "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "BaseModel class needs a docstring")

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

    def test_instance_creation(self):
        """Test if BaseModel is an instance of the BaseModel class"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_creation(self):
        """Test if BaseModel creates a unique ID"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """Test if created_at is of type datetime"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test if BaseModel has a string representation"""
        model = BaseModel()
        string_representation = str(model)
        self.assertEqual(string_representation, f"[BaseModel] ({model.id}) {model.__dict__}")

    @unittest.mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(initial_updated_at, new_updated_at)
        self.assertTrue(mock_storage.save.called)

    def test_reload(self):
        """Test if the reload function works for BaseModel"""
        model = BaseModel()
        model.save()
        initial_updated_at = model.updated_at
        model.reload()
        self.assertEqual(initial_updated_at, model.updated_at)

    def test_attributes(self):
        """Test if BaseModel has the expected attributes"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_save_to_file(self):
        """Test if BaseModel is saved to file"""
        model = BaseModel()
        model.save()
        file_path = "file.json"
        self.assertTrue(os.path.exists(file_path))

    def test_delete(self):
        """Test if the delete function works for BaseModel"""
        model = BaseModel()
        model.delete()
        self.assertNotIn(model, BaseModel)

    def test_new_instance(self):
        """Test if a new instance of BaseModel is created"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at value."""
        tic = datetime.utcnow()
        model1 = BaseModel()
        toc = datetime.utcnow()
        self.assertTrue(tic <= model1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.utcnow()
        model2 = BaseModel()
        toc = datetime.utcnow()
        self.assertTrue(tic <= model2.created_at <= toc)
        self.assertEqual(model1.created_at, model1.updated_at)
        self.assertEqual(model2.created_at, model2.updated_at)
        self.assertNotEqual(model1.created_at, model2.created_at)
        self.assertNotEqual(model1.updated_at, model2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        model1 = BaseModel()
        model2 = BaseModel()
        for inst in [model1, model2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIsInstance(uuid, str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(model1.id, model2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        new_dict = my_model.to_dict()
        expected_attributes = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(new_dict.keys(), expected_attributes)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['name'], "Holberton")
        self.assertEqual(new_dict['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = BaseModel()
        new_dict = my_model.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], my_model.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], my_model.updated_at.strftime(t_format))

if __name__ == '__main__':
    unittest.main
