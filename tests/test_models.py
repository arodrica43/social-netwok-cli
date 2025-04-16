import unittest
from domain.models import User

class TestUserModel(unittest.TestCase):
    """
    Unit tests for the User model.
    """
    
    def test_user_creation(self):
        user = User("Alice")
        self.assertEqual(user.username, "Alice")
        self.assertEqual(user.posts, [])
        self.assertEqual(user.follows, set())

    def test_post(self):
        user = User("Bob")
        user.post("Hello!")
        self.assertEqual(len(user.posts), 1)
        self.assertEqual(user.posts[0][0], "Hello!")

    def test_follow(self):
        user = User("Charlie")
        user.follow("David")
        self.assertIn("David", user.follows)

if __name__ == "__main__":
    unittest.main()
