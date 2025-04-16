"""
Domain models for the social network application.
"""

from datetime import datetime
from typing import List, Tuple, Set

class User:
    """
    Represents a user in the social network.
    """

    def __init__(self, username: str):
        self.username: str = username
        self.posts: List[Tuple[str, datetime]] = []
        self.follows: Set[str] = set()

    def post(self, message: str):
        """
        Adds a post to the user's timeline.

        Args:
            message (str): The content to post.
        """
        self.posts.append((message, datetime.now()))

    def follow(self, other_user: str):
        """
        Follows another user.

        Args:
            other_user (str): The username to follow.
        """
        self.follows.add(other_user)