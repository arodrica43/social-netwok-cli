"""
User repository interface and in-memory implementation.
"""

from domain.models import User

class UserRepository:
    """
    In-memory user repository. Can be replaced with a persistent version later.
    """

    def __init__(self):
        self.users = {}

    def get_or_create(self, username: str) -> User:
        """
        Retrieves a user or creates one if not found.

        Args:
            username (str): The name of the user.

        Returns:
            User: The corresponding user instance.
        """
        if username not in self.users:
            self.users[username] = User(username)
        return self.users[username]

    def get(self, username: str) -> User:
        """
        Retrieves a user by name.

        Args:
            username (str): The username to retrieve.

        Returns:
            User: The user instance, or None if not found.
        """
        return self.users.get(username)