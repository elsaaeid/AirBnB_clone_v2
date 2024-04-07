#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


def setUpModule():
    """ """
    pass


def tearDownModule():
    """ """
    pass


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set up a variable """
        self.my_model = BaseModel()
        self.file_storage = FileStorage()
        print("setUp")

    def tearDown(self):
        """ Clean up after test cases """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean up a Class"""
        print("tearDownClass")

    def fileStorageTest(self):
        """ Check the documentation of file storage """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def fileStorageExistTest(self):
        """ Check if the file storage exists """
        self.assertTrue(hasattr(self.file_storage, "__init__"))
        self.assertTrue(hasattr(self.file_storage, "all"))
        self.assertTrue(hasattr(self.file_storage, "new"))
        self.assertTrue(hasattr(self.file_storage, "save"))
        self.assertTrue(hasattr(self.file_storage, "reload"))

    def modelsSaveTest(self):
        """ Check if the save of function works """
        self.my_model.name = "Hello"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Hello")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
