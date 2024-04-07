#!/usr/bin/python3

import unittest
import os
from models.city import City


def setUpModule():
    """It is a function to set a module"""

    pass


def tearDownModule():
    """ It is a function to delete a module"""

    pass


class TestModels(unittest.TestCase):
    """It is a function to test the BaseModel."""

    def setUp(self):
        """This sets a variable."""

        self.city_test = City()
        self.city_test.state_id = "100"
        print("setUp")

    def tearDown(self):
        """This ends variable."""

        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """This defines class."""

        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """This closes the class."""

        print("tearDownClass")

    def cityDocumetationTest(self):
        """This checks the documentation."""

        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def cityExistTest(self):
        """This checks if the city methods exists."""

        self.city_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.city_test, "__init__"))
        self.assertTrue(hasattr(self.city_test, "state_id"))
        self.assertTrue(hasattr(self.city_test, "name"))

    def cityNameTest(self):
        """This checks if the name is created."""

        self.city_test.name = 'Paris'
        self.assertEqual(self.city_test.name, 'Paris')

    def modelsToDictTest(self):
        """test the to_dict method of BaseModel class"""

        my_dict = self.city_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["state_id"], str)
        self.assertIsInstance(my_dict["id"], str)

    def cityInstanceTest(self):
        """This checks if city_test is instance of City."""
        self.assertIsInstance(self.city_test, City)


if __name__ == '__main__':
    unittest.main()
