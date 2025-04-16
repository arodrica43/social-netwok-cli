"""
Utility functions for handling and validating CLI user input.
"""

from enum import Enum

class CommandType(Enum):
    POST = "POST"
    READ = "READ"
    FOLLOW = "FOLLOW"
    WALL = "WALL"
    EXIT = "EXIT"
    UNKNOWN = "UNKNOWN"

def validate_post_command(user_input: str) -> bool:
    """
    Validates the format of a post command.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    parts = user_input.split("->")
    if len(parts) != 2:
        return False
    username, message = parts
    return bool(username.strip()) and bool(message.strip())

def validate_read_command(user_input: str) -> bool:
    """
    Validates the format of a read command.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    parts = user_input.split(" ")
    return len(parts) == 1 and bool(parts[0].strip())

def validate_follow_command(user_input: str) -> bool:
    """
    Validates the format of a follow command.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    parts = user_input.split(" ")
    return len(parts) == 3 and parts[1].lower() == "follows" and bool(parts[0].strip()) and bool(parts[2].strip())

def validate_wall_command(user_input: str) -> bool:
    """
    Validates the format of a wall command.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    parts = user_input.split(" ")
    return len(parts) == 2 and bool(parts[0].strip()) and parts[1].lower() == "wall"

def validate_exit_command(user_input: str) -> bool:
    """
    Validates the format of an exit command.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        bool: True if the command is valid, False otherwise.
    """
    return user_input.strip().lower() in {"exit", "quit"}

def detect_command_type(user_input: str) -> CommandType:
    """
    Determines the type of command based on user input.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        CommandType: Enum representing the detected command.
    """
    cmd = user_input.strip()
    if not cmd:
        return CommandType.UNKNOWN
    if validate_exit_command(cmd):
        return CommandType.EXIT
    if validate_post_command(cmd):
        return CommandType.POST
    if validate_follow_command(cmd):
        return CommandType.FOLLOW
    if validate_wall_command(cmd):
        return CommandType.WALL
    if validate_read_command(cmd):
        return CommandType.READ
    return CommandType.UNKNOWN