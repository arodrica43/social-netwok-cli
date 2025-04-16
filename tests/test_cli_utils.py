import unittest
from cli.utils import detect_command_type, CommandType

class TestCLIUtils(unittest.TestCase):
    """
    Unit tests for the CLI utility functions.
    """
    
    def test_valid_commands(self):
        self.assertEqual(detect_command_type("Alice -> Hi"), CommandType.POST)
        self.assertEqual(detect_command_type("Alice follows Bob"), CommandType.FOLLOW)
        self.assertEqual(detect_command_type("Alice wall"), CommandType.WALL)
        self.assertEqual(detect_command_type("Alice"), CommandType.READ)
        self.assertEqual(detect_command_type("exit"), CommandType.EXIT)
        self.assertEqual(detect_command_type("quit"), CommandType.EXIT)

    def test_invalid_commands(self):
        self.assertEqual(detect_command_type(""), CommandType.UNKNOWN)
        self.assertEqual(detect_command_type("Hello world"), CommandType.UNKNOWN)
        self.assertEqual(detect_command_type("Alice does something"), CommandType.UNKNOWN)

if __name__ == "__main__":
    unittest.main()
