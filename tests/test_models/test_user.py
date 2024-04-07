#!/usr/bin/python3
import unittest
import os
from models.user import User


def setUpModule():
    """ Funtion to set up a Module """
    pass


def tearDownModule():
    """ Function to clean up a Module """
    pass


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel """
    def setUp(self):
        """ Set up a variable """
        self.user_test = User()
        self.user_test.first_name = 'Said'
        self.user_test.last_name = "Ellithy"
        self.user_test.email = 'saidsadaoy@gmail.com'
        self.user_test.password = "root"
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

    def userTest(self):
        """ Check if user exists """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def userPropertiesTest(self):
        """ Check if the user properties are created """
        self.user_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_test, "__init__"))
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertTrue(hasattr(self.user_test, "last_name"))
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertTrue(hasattr(self.user_test, "password"))

    def userFirstNameTest(self):
        """ Check if the first name is created """
        self.assertEqual(self.user_test.first_name, 'Said')

    def userLastNameTest(self):
        """ Chaeck if the last name is created """
        self.assertEqual(self.user_test.last_name, "Ellithy")

    def userEmailTest(self):
        """ Chaeck if the email is created """
        self.assertEqual(self.user_test.email, 'saidsadaoy@gmail.com')

    def userPasswordTest(self):
        """ Chaeck if the password is created """
        self.assertEqual(self.user_test.password, "root")

    def modelsToDictTest(self):
        """ Check the converting to dict """
        my_dict = self.user_test.to_dict()
        self.assertIsInstance(my_dict["id"], str)
        self.assertIsInstance(my_dict["email"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)

    def userInstanceTest(self):
        """ Check if user_test is instance of User """
        self.assertIsInstance(self.user_test, User)


if __name__ == '__main__':
    unittest.main()
