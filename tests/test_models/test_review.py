#!/usr/bin/python3
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.review = Review()

    def tearDown(self):
        """Clean up after test cases"""
        del self.review

    def test_review_instance(self):
        """Test if Review is an instance of the Review class"""
        self.assertIsInstance(self.review, Review)

    def test_review_attributes(self):
        """Test Review attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_save(self):
        """Test if the save function works for Review"""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "This is a test review"
        self.review.save()
        all_reviews = storage.all(Review)
        review_key = "Review." + self.review.id
        self.assertIn(review_key, all_reviews)

    def test_review_to_dict(self):
        """Test if the to_dict function works for Review"""
        review_dict = self.review.to_dict()
        self.assertEqual(self.review.__class__.__name__, 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_review_storage(self):
        """Test if Review is correctly stored in the storage"""
        storage.new(self.review)
        storage.save()
        all_reviews = storage.all(Review)
        review_key = "Review." + self.review.id
        self.assertIn(review_key, all_reviews)

    def test_review_delete(self):
        """Test if the delete function works for Review"""
        review_id = self.review.id
        storage.new(self.review)
        storage.save()
        storage.delete(self.review)
        all_reviews = storage.all(Review)
        review_key = "Review." + review_id
        self.assertNotIn(review_key, all_reviews)


if __name__ == '__main__':
    unittest.main()
