#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review
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

    def test_pep8_equality(self):
        """Test that review.py and test_review.py conform to PEP8"""
        files_to_check = ['models/review.py',
                          'tests/test_models/test_review.py']
        style_guide = pep8.StyleGuide()
        total_errors = 0
        error_messages = []

        for file_path in files_to_check:
            with self.subTest(path=file_path):
                result = style_guide.check_files([file_path])
                errors = result.total_errors

                if errors > 0:
                    print(f"PEP8 errors in {file_path}:")
                    for error in result.messages:
                        error_messages.append(f"- {error}")
                total_errors += errors
        if total_errors > 0:
            error_message = f"Total PEP8 errors: {total_errors}\n"
            error_message += "\n".join(error_messages)
            self.fail(error_message)

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
        """Test that Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.review = Review()

    def test_review_attributes(self):
        """Test Review attributes"""
        review = self.review
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        if models.storage_type == 'db':
            self.assertIsNone(review.place_id)
            self.assertIsNone(review.user_id)
            self.assertIsNone(review.text)
        else:
            self.assertEqual(review.place_id, "")
            self.assertEqual(review.user_id, "")
            self.assertEqual(review.text, "")

    def test_to_dict(self):
        """test to_dict method creates a dictionary"""
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in review.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         review.created_at.strftime(format_t))
        self.assertEqual(new_dict["updated_at"],
                         review.updated_at.strftime(format_t))

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

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_updated_at_save(self):
        """Test function to save updated_at attribute"""
        self.review.save()
        actual = type(self.review.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

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
