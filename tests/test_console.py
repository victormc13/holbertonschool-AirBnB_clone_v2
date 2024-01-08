import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance and redirect stdout for testing."""
        self.console = HBNBCommand()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore the original stdout after testing."""
        sys.stdout = self.saved_stdout

    def test_create(self):
        """Test the create command."""
        command = "create BaseModel"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)

    def test_show(self):
        """Test the show command."""
        command = "show BaseModel 1234-1234-1234"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test the destroy command."""
        command = "destroy BaseModel 1234-1234-1234"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test the all command."""
        command = "all BaseModel"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "[]")

    def test_count(self):
        """Test the count command."""
        command = "count BaseModel"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "0")

    def test_update(self):
        """Test the update command."""
        command = "update BaseModel 1234-1234-1234 name 'John Doe'"
        self.console.onecmd(command)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
