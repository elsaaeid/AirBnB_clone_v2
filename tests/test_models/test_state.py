#!/usr/bin/python3
import unittest
from models.state import State
from models import storage
import pep8
import inspect
from models import state
from models.base_model import BaseModel
import models


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_functions = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_equality_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_equality_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(State.__doc__, None, "state.py needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1, "state.py needs a docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None, "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1, "State class needs a docstring")

    def test_state_func_docstring(self):
        """Test for the presence of docstrings in State methods"""
        for func_name, func in self.state_functions:
            self.assertIsNot(func.__doc__, None, f"{func_name} method needs a docstring")
            self.assertTrue(len(func.__doc__) >= 1, f"{func_name} method needs a docstring")



class TestState(unittest.TestCase):
    """Test the State class"""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

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

    def test_to_dict_creates_dict(self):
        """Test if to_dict method creates a dictionary with proper attributes"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

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
        all_states = storage.all(State)
        state_key = "State." + state.id
        self.assertIn(state_key, all_states)

    def test_state_to_dict(self):
        """Test if the to_dict function works for State"""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state.__class__.__name__, 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_storage(self):
        """Test if State is correctly stored in the storage"""
        state = State()
        storage.new(state)
        storage.save()
        all_states = storage.all(State)
        state_key = "State." + state.id
        self.assertIn(state_key, all_states)

    def test_state_delete(self):
        """Test if the delete function works for State"""
        state = State()
        state_id = state.id
        storage.new(state)
        storage.save()
        storage.delete(state)
        all_states = storage.all(State)
        state_key = "State." + state_id
        self.assertNotIn(state_key, all_states)

if __name__ == '__main__':
    unittest.main()
