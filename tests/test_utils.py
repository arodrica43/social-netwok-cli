import unittest
from utils.time import format_timedelta
from datetime import datetime, timedelta

class TestTimeUtils(unittest.TestCase):
    """
    Test cases for the time utility functions.
    """
    
    def test_seconds(self):
        ts = datetime.now() - timedelta(seconds=59)
        self.assertEqual(format_timedelta(ts), "59 seconds ago")

    def test_minutes(self):
        ts = datetime.now() - timedelta(minutes=3)
        self.assertEqual(format_timedelta(ts), "3 minutes ago")

    def test_hours(self):
        ts = datetime.now() - timedelta(hours=2)
        self.assertEqual(format_timedelta(ts), "2 hours ago")

if __name__ == "__main__":
    unittest.main()
