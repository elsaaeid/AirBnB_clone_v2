#!/usr/bin/python3
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.place = Place()

    def tearDown(self):
        """Clean up after test cases"""
        del self.place

    def test_place_instance(self):
        """Test if Place is an instance of the Place class"""
        self.assertIsInstance(self.place, Place)

    def test_place_attributes(self):
        """Test Place attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_save(self):
        """Test if the save function works for Place"""
        self.place.name = "Test Place"
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.save()
        all_places = storage.all(Place)
        place_key = "Place." + self.place.id
        self.assertIn(place_key, all_places)

    def test_place_to_dict(self):
        """Test if the to_dict function works for Place"""
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.__class__.__name__, 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_storage(self):
        """Test if Place is correctly stored in the storage"""
        storage.new(self.place)
        storage.save()
        all_places = storage.all(Place)
        place_key = "Place." + self.place.id
        self.assertIn(place_key, all_places)

    def test_place_delete(self):
        """Test if the delete function works for Place"""
        place_id = self.place.id
        storage.new(self.place)
        storage.save()
        storage.delete(self.place)
        all_places = storage.all(Place)
        place_key = "Place." + place_id
        self.assertNotIn(place_key, all_places)


if __name__ == '__main__':
    unittest.main()
