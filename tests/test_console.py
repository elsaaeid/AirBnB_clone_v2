#!/usr/bin/python3
import console
import pep8
import unittest
from io import StringIO

from unittest.mock import patch
HBNBCommand = console.HBNBCommand


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
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_count(self):
        """Test the "count" command for BaseModel"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_show(self):
        """Test the "show" command for BaseModel"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_destroy(self):
        """Test the "destroy" command for BaseModel"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_update(self):
        """Test the "update" command for BaseModel"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_all(self):
        """Test the "all" command for Amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            expected_output = "<expected output from the all command>"
            self.assert_stdout("all Amenity", expected_output)
            self.assertEqual(expected_output.strip(), f.getvalue().strip())

    def test_amenity_count(self):
        """Test the "count" command for Amenity"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_show(self):
        """Test the "show" command for Amenity"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_destroy(self):
        """Test the "destroy" command for Amenity"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_update(self):
        """Test the "update" command for Amenity"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_all(self):
        """Test the "all" command for City"""
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_count(self):
        """Test the "count" command for City"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_show(self):
        """Test the "show" command for City"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_destroy(self):
        """Test the "destroy" command for City"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_update(self):
        """Test the "update" command for City"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_all(self):
        """Test the "all" command for Place"""
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_count(self):
        """Test the "count" command for Place"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)


    def test_place_show(self):
        """Test the "show" command for Place"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_destroy(self):
        """Test the "destroy" command for Place"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_update(self):
        """Test the "update" command for Place"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_all(self):
        """Test the "all" command for Review"""
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_count(self):
        """Test the "count" command for Review"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_show(self):
        """Test the "show" command for Review"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_destroy(self):
        """Test the "destroy" command for Review"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_update(self):
        """Test the "update" command for Review"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_all(self):
        """Test the "all" command for State"""
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_count(self):
        """Test the "count" command for State"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_show(self):
        """Test the "show" command for State"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_destroy(self):
        """Test the "destroy" command for State"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_update(self):
        """Test the "update" command for State"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_all(self):
        """Test the "all" command for User"""
        expected_output = "<expected output from the all command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_count(self):
        """Test the "count" command for User"""
        expected_output = "<expected output from the count command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_show(self):
        """Test the "show" command for User"""
        expected_output = "<expected output from the show command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_destroy(self):
        """Test the "destroy" command for User"""
        expected_output = "<expected output from the destroy command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 12345-6789")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_update(self):
        """Test the "update" command for User"""
        expected_output = "<expected output from the update command>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), expected_output)
