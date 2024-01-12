import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
import MySQLdb


class TestHBNBCommandMethods(unittest.TestCase):

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.do_create("User name=\"John\" age=25")
            output = mock_stdout.getvalue().strip()
            self.assertIsInstance(output, str)

    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.do_all("User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("["))

    def test_params_format(self):
        params = ['name="John"', 'age=25']
        result = self.hbnb_cmd._params_format(params)
        expected_result = {'name': 'John', 'age': 25}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
