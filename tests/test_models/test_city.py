#!/usr/bin/python3
import unittest
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.city = City()

    def tearDown(self):
        """Clean up after test cases"""
        del self.city

    def test_city_instance(self):
        """Test if City is an instance of the City class"""
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """Test City attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_city_save(self):
        """Test if the save function works for City"""
        self.city.name = "Test City"
        self.city.state_id = "123"
        self.city.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_to_dict(self):
        """Test if the to_dict function works for City"""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_storage(self):
        """Test if City is correctly stored in the storage"""
        storage.new(self.city)
        storage.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_delete(self):
        """Test if the delete function works for City"""
        city_id = self.city.id
        storage.new(self.city)
        storage.save()
        storage.delete(self.city)
        all_cities = storage.all(City)
        city_key = "City." + city_id
        self.assertNotIn(city_key, all_cities)


if __name__ == '__main__':
    unittest.main()
