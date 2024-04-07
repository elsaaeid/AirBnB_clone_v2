#!/usr/bin/python3
import unittest
import os
from models.place import Place


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
        self.place_test = Place()
        self.place_test.number_bathrooms = 1
        self.place_test.longitude = 10.10
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

    def placeTest(self):
        """ Check place documentation """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def placeExistTest(self):
        """ Check if the place properties are created """
        self.place_test.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.place_test, "__init__"))
        self.assertTrue(hasattr(self.place_test, "city_id"))
        self.assertTrue(hasattr(self.place_test, "user_id"))
        self.assertTrue(hasattr(self.place_test, "name"))
        self.assertTrue(hasattr(self.place_test, "description"))
        self.assertTrue(hasattr(self.place_test, "number_rooms"))
        self.assertTrue(hasattr(self.place_test, "number_bathrooms"))
        self.assertTrue(hasattr(self.place_test, "max_guest"))
        self.assertTrue(hasattr(self.place_test, "price_by_night"))
        self.assertTrue(hasattr(self.place_test, "latitude"))
        self.assertTrue(hasattr(self.place_test, "longitude"))
        self.assertTrue(hasattr(self.place_test, "amenity_ids"))

    def modelToDictTest(self):
        """ Check converting to dict """
        my_dict = self.place_test.to_dict()
        self.assertIsInstance(my_dict["id"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["number_bathrooms"], int)
        self.assertIsInstance(my_dict["longitude"], float)

    def placeIsInstanceTest(self):
        """ Check if place_test is instance of Place """
        self.assertIsInstance(self.place_test, Place)


if __name__ == '__main__':
    unittest.main()
