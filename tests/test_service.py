import unittest
from service.social_network import SocialNetworkService
from cli.utils import detect_command_type, CommandType

class TestSocialNetworkService(unittest.TestCase):
    """
    Unit tests for the SocialNetworkService class.
    """
    
    def setUp(self):
        self.sn = SocialNetworkService()
    
    def _test_command(self, command):
        command_type = detect_command_type(command)
        result = self.sn.handle_command(command_type, command)
        return result

    def test_post_command(self):
        self._test_command("Alice -> Hello World")
        output = self._test_command("Alice")
        self.assertIn("Hello World", output)

    def test_read_no_posts(self):
        result = self._test_command("Ghost")
        self.assertEqual(result, "Ghost has not posted anything yet.")

    def test_follow_command(self):
        self._test_command("Bob -> First")
        self._test_command("Charlie follows Bob")
        output = self._test_command("Charlie wall")
        self.assertIn("Bob - First", output)

    def test_wall_unknown_user(self):
        result = self._test_command("Nobody wall")
        self.assertEqual(result, "Nobody does not exist.")

    def test_invalid_follow_format(self):
        result = self._test_command("X follows")
        self.assertEqual(result, "Unknown command.")

    def test_invalid_post_format(self):
        result = self._test_command("X ->")
        self.assertEqual(result, "Unknown command.")

    def test_invalid_wall_format(self):
        result = self._test_command(" wall")
        self.assertEqual(result, "wall has not posted anything yet.")

    def test_malformed_command(self):
        result = self._test_command("totally wrong format")
        self.assertEqual(result, "Unknown command.")

    def test_exit_command(self):
        result = self._test_command("exit")
        self.assertEqual(result, "EXIT")

if __name__ == "__main__":
    unittest.main()
