#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.amenity = Amenity(name="Test Amenity")

    def tearDown(self):
        """Clean up after test cases"""
        del self.amenity

    def test_amenity_instance(self):
        """Test if Amenity is an instance of the Amenity class"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_save(self):
        """Test if the save function works for Amenity"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        """Test if the to_dict function works for Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(self.amenity.__class__.__name__, 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_storage(self):
        """Test if Amenity is correctly stored in the storage"""
        storage.new(self.amenity)
        storage.save()
        all_amenities = storage.all(Amenity)
        amenity_key = "Amenity." + self.amenity.id
        self.assertIn(amenity_key, all_amenities)

    def test_amenity_delete(self):
        """Test if the delete function works for Amenity"""
        amenity_id = self.amenity.id
        storage.new(self.amenity)
        storage.save()
        storage.delete(self.amenity)
        all_amenities = storage.all(Amenity)
        amenity_key = "Amenity." + amenity_id
        self.assertNotIn(amenity_key, all_amenities)


if __name__ == '__main__':
    unittest.main()
