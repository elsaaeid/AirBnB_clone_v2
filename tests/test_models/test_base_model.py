#!/usr/bin/python3

import models
import unittest
import os
from datetime import datetime
from models.__init__ import storage
from models.base_model import BaseModel


def setUpModule():
    """ """
    pass


def tearDownModule():
    """ """
    pass


class TestModels(unittest.TestCase):
    """ This is a unittests of testing instantiation of BaseModel class """
    def setUp(self):
        """ Set up a variable """

        self.my_model = BaseModel()
        self.my_model.my_number = 29
        print("setUp")

    def tearDown(self):
        """ Clean up variable """

        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up a class """

        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean up a class """

        print("tearDownClass")

    def modelsDocumentTest(self):
        """ Checks the documentation."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def modelsNameTest(self):
        """ This checks if name is created """
        self.my_model.name = 'test'
        self.assertEqual(self.my_model.name, 'test')

    def modelsNumberTest(self):
        """This checks if the number is created."""
        self.assertEqual(self.my_model.my_number, 29)

    def modelsExistTest(self):
        """ This checks if the json file and methods are existed."""

        self.my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.my_model, "__init__"))
        self.assertTrue(hasattr(self.my_model, "__str__"))
        self.assertTrue(hasattr(self.my_model, "save"))
        self.assertTrue(hasattr(self.my_model, "to_dict"))

    def modelsNonEmptyTest(self):
        """This checks if the json file is not empty."""
        self.assertTrue('file.json')

    def modelsSaveTest(self):
        """This checks if the save function works."""
        a = self.my_model.updated_at()
        self.my_model.save()
        self.assertNotEqual(a, self.my_model.update_at)
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

    def modelsInstanceTest(self):
        """This checks if user_test is instance of user."""
        self.assertIsInstance(self.my_model, BaseModel)

    def modelsToDictTest(self):
        """test the to_dict method of the BaseModel class"""
        my_dict = self.my_model.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["my_number"], int)
        self.assertIsInstance(my_dict["id"], str)


if __name__ == '__main__':
    unittest.main()
