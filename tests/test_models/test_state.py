#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime
from models import storage
import pep8
import inspect
from models.base_model import BaseModel
import models


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_functions = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that state.py and test_state.py conform to PEP8"""
        files_to_check = ['models/state.py',
                          'tests/test_models/test_state.py']
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

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(
            State.__doc__,
            None,
            "state.py needs a docstring"
        )
        self.assertTrue(
            len(State.__doc__) >= 1,
            "state.py needs a docstring"
        )

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(
            State.__doc__,
            None,
            "State class needs a docstring"
        )
        self.assertTrue(
            len(State.__doc__) >= 1,
            "State class needs a docstring"
        )

    def test_state_func_docstring(self):
        """Test for the presence of docstrings in State methods"""
        for func_name, func in self.state_functions:
            self.assertIsNot(
                func.__doc__,
                None,
                f"{func_name} method needs a docstring"
            )
            self.assertTrue(
                len(func.__doc__) >= 1,
                f"{func_name} method needs a docstring"
            )


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def setUp(self):
        """Set up the test environment"""
        self.state = State()

    def test_state_instance(self):
        """Test if State is an instance of the State class"""
        state = State()
        self.assertIsInstance(state, State)

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if models.storage_type == 'db':
            self.assertIsNone(state.name)
        else:
            self.assertEqual(state.name, "")

    def test_to_dict(self):
        """Test if to_dict method creates a dictionary"""
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertNotIn("_sa_instance_state", new_dict)
        for attr in state.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_dict)
        self.assertIn("__class__", new_dict)

    def test_to_dict_values(self):
        """Test that values in to_dict are correct
        """
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         state.created_at.strftime(format_t))
        self.assertEqual(new_dict["updated_at"],
                         state.updated_at.strftime(format_t))

    def test_str(self):
        """Test that the str method has the correct output"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_state_save(self):
        """Test if the save function works for State"""
        state = State()
        state.name = "Test State"
        state.save()
        all_states = models.storage.all(State)
        state_key = "State." + state.id
        self.assertIn(state_key, all_states)

    @unittest.skipIf(models.storage_type == 'db', 'skip if environ is db')
    def test_updated_at_save(self):
        """Test function to save updated_at attribute"""
        self.state.save()
        actual = type(self.state.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_state_storage(self):
        """Test if State is correctly stored in the storage"""
        state = State()
        models.storage.new(state)
        models.storage.save()
        all_states = models.storage.all(State)
        state_key = "State." + state.id
        self.assertIn(state_key, all_states)

    def test_state_delete(self):
        """Test if the delete function works for State"""
        state = State()
        state_id = state.id
        models.storage.new(state)
        models.storage.save()
        models.storage.delete(state)
        all_states = models.storage.all(State)
        state_key = "State." + state_id
        self.assertNotIn(state_key, all_states)

if __name__ == '__main__':
    unittest.main()
