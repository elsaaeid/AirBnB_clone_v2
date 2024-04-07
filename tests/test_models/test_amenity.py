#!/usr/bin/python3
import unittest
import os
from models.amenity import Amenity


def setUpModule():
    """It is a function to set module"""
    pass


def tearDownModule():
    """It is function to delete module """
    pass


class TestModels(unittest.TestCase):
    """ It is function to test the BaseModel."""

    def setUp(self):
        """This sets a variable."""

        self.amenity_test = Amenity()
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

    def amenityDocumentTest(self):
        """This checks the documetation."""

        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def placeCityTest(self):
        """ This checks the amenity methods exists."""

        self.amenity_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.amenity_test, "__init__"))
        self.assertTrue(hasattr(self.amenity_test, "name"))

    def amenityNameTest(self):
        """This checks if the name is created."""

        self.amenity_test.name = 'Good'
        self.assertEqual(self.amenity_test.name, 'Good')

    def modelsToDictTest(self):
        """ test the to_dict method of BaseModel class"""

        my_dict = self.amenity_test.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["id"], str)

    def amenityInstanceTest(self):
        """This checks if amenity_test is instance of Amenity."""

        self.assertIsInstance(self.amenity_test, Amenity)


if __name__ == '__main__':
    unittest.main()
