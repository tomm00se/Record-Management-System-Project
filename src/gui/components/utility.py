"""Utility functions for GUI"""

from datetime import datetime

class DateFormatter:
    """ Convert date string to display format """
    @staticmethod
    def to_display_format(date_string, input_format="%Y-%m-%dT%H:%M:%S.%f", output_format="%d %b %Y"):
        """Convert date string to display format"""
        try:
            date_obj = datetime.strptime(date_string, input_format)
            return date_obj.strftime(output_format)
        except Exception as e:
            print(f"Error formatting date: {e}")
            return date_string
