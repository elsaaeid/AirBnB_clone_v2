#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test"""
        del self.console

    def test_docstring_file(self):
        """Test the docstring of the console module"""
        expected_docstring = "Command interpreter for Holberton AirBnB project"
        actual_docstring = self.console.__class__.__doc__
        self.assertEqual(expected_docstring, actual_docstring)

    def test_docstring_class(self):
        """Test the docstring of the HBNBCommand class"""
        expected_docstring = "Command interpreter class"
        actual_docstring = HBNBCommand.__doc__
        self.assertEqual(expected_docstring, actual_docstring)

    def test_emptyline(self):
        """Test the behavior of the emptyline method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.emptyline()
            self.assertEqual(fake_out.getvalue(), "")

    def test_help(self):
        """Test the behavior of the help command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", fake_out.getvalue())

    def test_exit(self):
        """Test the behavior of the exit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertIn("Quit command is called", fake_out.getvalue())

    def test_unknown_command(self):
        """Test the behavior of an unknown command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("unknown_command")
            self.assertIn("unknown_command: command not found", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
