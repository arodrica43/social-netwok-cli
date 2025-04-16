import unittest
from domain.repository import UserRepository

class TestUserRepository(unittest.TestCase):
    """
    Unit tests for the UserRepository class.
    """
    
    def test_get_or_create_new(self):
        repo = UserRepository()
        user = repo.get_or_create("Alice")
        self.assertEqual(user.username, "Alice")

    def test_get_or_create_existing(self):
        repo = UserRepository()
        repo.get_or_create("Bob")
        user = repo.get_or_create("Bob")
        self.assertEqual(user.username, "Bob")

    def test_get_none(self):
        repo = UserRepository()
        self.assertIsNone(repo.get("Ghost"))

if __name__ == "__main__":
    unittest.main()
