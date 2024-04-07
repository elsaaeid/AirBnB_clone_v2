#!/usr/bin/python3
import unittest
import os
from models.state import State


def setUpModule():
    """ Funtion to set up a Module"""
    pass


def tearDownModule():
    """ Function to clean up a Module"""
    pass


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set up a variable """
        self.state_test = State()
        print("setUp")

    def tearDown(self):
        """ Clean up variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set up class """

        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Clean up the class """
        print("tearDownClass")

    def stateTest(self):
        """ Check the documentation """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def stateExistTest(self):
        """ Check if the state name exist """
        self.state_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.state_test, "__init__"))
        self.assertTrue(hasattr(self.state_test, "name"))

    def stateNameTest(self):
        """ Check if the state name is created """
        self.state_test.name = 'Great'
        self.assertEqual(self.state_test.name, 'Great')

    def modelsToDictTest(self):
        """ Check the converting to dict """
        my_dict = self.state_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def stateInstanceTest(self):
        """ Check if state_test is instance of State """
        self.assertIsInstance(self.my_dict, State)


if __name__ == '__main__':
    unittest.main()
