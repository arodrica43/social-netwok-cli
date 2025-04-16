"""
Service layer for orchestrating user actions in the social network.
"""

from domain.repository import UserRepository
from utils.time import format_timedelta
from cli.utils import CommandType

class SocialNetworkService:
    """
    Business logic for processing user commands in the social network.
    """

    def __init__(self, user_repo=None):
        self.user_repo = user_repo or UserRepository()

    def handle_command(self, command_type: CommandType, command: str) -> str:
        """
        Parses and handles a user command string using a typed representation.

        Args:
            command (str): User input string.

        Returns:
            str: Result of the command.
        """
        try:
            if command_type == CommandType.EXIT:
                return "EXIT"

            if command_type == CommandType.POST:
                user, message = map(str.strip, command.split("->", 1))
                return self._post(user, message)

            if command_type == CommandType.FOLLOW:
                user, target = map(str.strip, command.split("follows", 1))
                return self._follow(user, target)

            if command_type == CommandType.WALL:
                user = command.replace(" wall", "").strip()
                return self._wall(user)

            if command_type == CommandType.READ:
                return self._read(command.strip())

            return "Unknown command."

        except ValueError:
            return "Invalid command format."
        except Exception as e:
            return f"Error: {str(e)}"

    def _post(self, user: str, message: str) -> str:
        """
        Posts a new message.

        Args:
            user (str): User adding the post.
            message (str): Message content.

        Returns:
            str: Empty string if successful.
        """
        self.user_repo.get_or_create(user).post(message)
        return ""

    def _read(self, user: str) -> str:
        """
        Reads the posts of a user.

        Args:
            user (str): User whose posts to read.

        Returns:
            str: Formatted string of posts or a message if no posts exist.
        """
        user_obj = self.user_repo.get(user)
        if not user_obj or not user_obj.posts:
            return f"{user} has not posted anything yet."
        return "\n".join([
            f"{msg} ({format_timedelta(ts)})"
            for msg, ts in reversed(user_obj.posts)
        ])

    def _follow(self, user: str, target: str) -> str:
        """
        Follows another user.

        Args:
            user (str): User who wants to follow.
            target (str): User to be followed.

        Returns:
            str: Empty string if successful.
        """
        self.user_repo.get_or_create(user).follow(target)
        self.user_repo.get_or_create(target)
        return ""

    def _wall(self, user: str) -> str:
        """
        Displays the wall of a user, including their posts and the posts of users they follow.

        Args:
            user (str): User whose wall to display.
            
        Returns:
            str: Formatted string of posts or a message if the user does not exist.
        """
        user_obj = self.user_repo.get(user)
        if not user_obj:
            return f"{user} does not exist."
        messages = []
        users_to_show = user_obj.follows | {user_obj.username}
        for uname in users_to_show:
            u = self.user_repo.get(uname)
            if u:
                for msg, ts in u.posts:
                    messages.append((uname, msg, ts))
        messages.sort(key=lambda x: x[2], reverse=True)
        return "\n".join([
            f"{u} - {msg} ({format_timedelta(ts)})"
            for u, msg, ts in messages
        ])