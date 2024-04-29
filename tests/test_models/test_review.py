#!/usr/bin/python3
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import inspect
import models
from models.base_model import BaseModel
import pep8

class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_functions = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_equality_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(
            result.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_pep8_equality_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(
            result.total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(
            Review.__doc__,
            None,
            "review.py needs a docstring"
        )
        self.assertTrue(
            len(Review.__doc__) >= 1,
            "review.py needs a docstring"
        )

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(
            Review.__doc__,
            None,
            "Review class needs a docstring"
        )
        self.assertTrue(
            len(Review.__doc__) >= 1,
            "Review class needs a docstring"
        )

    def test_review_func_docstring(self):
        """Test for the presence of docstrings in Review methods"""
        for func_name, func in self.review_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )



class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_review_instance(self):
        """Test if Review is an instance of the Review class"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test Review attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        if models.storage_type == 'db':
            self.assertIsNone(self.review.place_id)
            self.assertIsNone(self.review.user_id)
            self.assertIsNone(self.review.text)
        else:
            self.assertEqual(self.review.place_id, "")
            self.assertEqual(self.review.user_id, "")
            self.assertEqual(self.review.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_review_save(self):
        """Test if the save function works for Review"""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "This is a test review"
        self.review.save()
        all_reviews = storage.all(Review)
        review_key = "Review." + self.review.id
        self.assertIn(review_key, all_reviews)

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
