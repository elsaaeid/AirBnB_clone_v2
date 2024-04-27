#!/usr/bin/python3
import unittest
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up a variable"""
        self.state = State()

    def tearDown(self):
        """Clean up after test cases"""
        del self.state

    def test_state_instance(self):
        """Test if State is an instance of the State class"""
        self.assertIsInstance(self.state, State)

    def test_state_attributes(self):
        """Test State attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_save(self):
        """Test if the save function works for State"""
        self.state.name = "Test State"
        self.state.save()
        all_states = storage.all(State)
        state_key = "State." + self.state.id
        self.assertIn(state_key, all_states)

    def test_state_to_dict(self):
        """Test if the to_dict function works for State"""
        state_dict = self.state.to_dict()
        self.assertEqual(self.state.__class__.__name__, 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_storage(self):
        """Test if State is correctly stored in the storage"""
        storage.new(self.state)
        storage.save()
        all_states = storage.all(State)
        state_key = "State." + self.state.id
        self.assertIn(state_key, all_states)

    def test_state_delete(self):
        """Test if the delete function works for State"""
        state_id = self.state.id
        storage.new(self.state)
        storage.save()
        storage.delete(self.state)
        all_states = storage.all(State)
        state_key = "State." + state_id
        self.assertNotIn(state_key, all_states)


if __name__ == '__main__':
    unittest.main()
