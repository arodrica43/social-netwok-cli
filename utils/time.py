"""
Utility functions for time formatting.
"""

from datetime import datetime

def format_timedelta(ts: datetime) -> str:
    """
    Formats the difference between now and a given timestamp.

    Args:
        ts (datetime): The timestamp to compare against now.

    Returns:
        str: Human-readable string representing the time difference.
    """
    delta = datetime.now() - ts
    seconds = int(delta.total_seconds())

    if seconds < 60:
        return f"{seconds} seconds ago"
    elif seconds < 3600:
        return f"{seconds // 60} minutes ago"
    else:
        return f"{seconds // 3600} hours ago"