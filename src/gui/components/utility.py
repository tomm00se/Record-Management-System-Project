"""Utility functions for GUI"""
from datetime import datetime
from tkinter import Entry

class DateFormatter:
    """Date formatting utility class"""

    @staticmethod
    def to_display_format(date_string):
        """
        Convert any date string to display format (DD MMM YYYY)
        Handles multiple input formats
        """
        # List of possible input formats
        input_formats = [
            "%Y-%m-%dT%H:%M:%S.%f",  # For created_at timestamp
            "%d/%m/%Y",              # For DD/MM/YYYY format
            "%d %b %Y"               # Already in display format
        ]

        for date_format in input_formats:
            try:
                date_obj = datetime.strptime(date_string, date_format)
                return date_obj.strftime("%d %b %Y")
            except ValueError:
                continue

        # If no format matches, return original string
        return date_string

    @staticmethod
    def is_valid_date(date_string):
        """Check if the date string is in a valid format"""
        try:
            datetime.strptime(date_string, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def format_date_entry(entry: Entry):
        """Format date as DD/MM/YYYY while typing"""
        text = entry.get()

        # Remove any non-digit characters
        cleaned_text = ''.join(filter(str.isdigit, text))

        # Limit to 8 digits (DDMMYYYY)
        cleaned_text = cleaned_text[:8]

        formatted_date = ""

        # Format the date with slashes
        if len(cleaned_text) > 0:
            # Add day
            day = cleaned_text[:2] if len(cleaned_text) >= 2 else cleaned_text
            # Ensure day is not > 31
            if len(day) == 2 and int(day) > 31:
                day = "31"
            formatted_date += day

            # Add month
            if len(cleaned_text) > 2:
                month = cleaned_text[2:4]
                # Ensure month is not > 12
                if len(month) == 2 and int(month) > 12:
                    month = "12"
                formatted_date += "/" + month

            # Add year
            if len(cleaned_text) > 4:
                formatted_date += "/" + cleaned_text[4:]

        # Update entry content
        entry.delete(0, 'end')
        entry.insert(0, formatted_date)
