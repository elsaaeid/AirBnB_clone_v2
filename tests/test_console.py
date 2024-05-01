#!/usr/bin/python3
import console
import pep8
import unittest
HBNBCommand = console.HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_equality(self):
        """Test that console.py and test_console.py conform to PEP8"""
        files_to_check = ['console.py',
                          'tests/test_console.py']
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

    def test_console_module_docstring(self):
        """Test for the console.py module"""
        self.assertIsNot(
            console.__doc__,
            None,
            "console.py needs a docstring"
        )
        self.assertTrue(
            len(console.__doc__) >= 1,
            "console.py needs a docstring"
        )

    def test_console_class_docstring(self):
        """Test for the class console"""
        self.assertIsNot(
            HBNBCommand.__doc__,
            None,
            "HBNBCommand class needs a docstring"
        )
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring"
        )


class TestConsole(unittest.TestCase):
    def assert_stdout(self, command, expected_output):
        """Helper method to assert the captured
        stdout matches the expected output
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_all(self):
        """Test the "all" command for BaseModel"""
        self.assert_stdout("all BaseModel",
                           "<expected output from the all command>")

    def test_review_all(self):
        """Test the "all" command for Review"""
        self.assert_stdout("all Review", 
                           "<expected output from the all command>")

    def test_user_all(self):
        """Test the "all" command for User"""
        self.assert_stdout("all User", "<expected output from the all command>")

    def test_state_all(self):
        """Test the "all" command for State"""
        self.assert_stdout("all State",
                           "<expected output from the all command>")

    def test_city_all(self):
        """Test the "all" command for City"""
        self.assert_stdout("all City",
                           "<expected output from the all command>")

    def test_amenity_all(self):
        """Test the "all" command for Amenity"""
        self.assert_stdout("all Amenity",
                           "<expected output from the all command>")

    def test_place_all(self):
        """Test the "all" command for Place"""
        self.assert_stdout("all Place",
                           "<expected output from the all command>")

    def test_count_command(self):
        """Test the "count" command for BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(),
                             "<expected output from the count command>")

    def test_show_command(self):
        """Test the "show" command for BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12345-6789")
            self.assertEqual(f.getvalue().strip(),
                             "<expected output from the show command>")

    def test_destroy_command(self):
        """Test the "destroy" command for BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345-6789")
            self.assertEqual(f.getvalue().strip(),
                             "<expected output from the destroy command>")

    def test_update_command(self):
        """Test the "update" command for BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345-6789 attribute_name string_value")
            self.assertEqual(f.getvalue().strip(),
                             "<expected output from the update command>")
