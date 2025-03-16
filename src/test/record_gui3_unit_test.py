import sys
import unittest
from unittest.mock import MagicMock
import tkinter as tk
import customtkinter as ctk
from src.gui.record_gui3 import  RecordMgmtSystem


class TestRecordMgmtSystem(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment."""
        self.root = ctk.CTk()  # Create the root window
        self.app = RecordMgmtSystem(self.root)  # Create an instance of the app

    def test_initialization(self):
        """Test that the application initializes with correct settings."""
        self.assertEqual(self.root.title(), "Record Management System")
        self.assertEqual(self.root.geometry(), "1280x768")

        # Test if main content and sidebar exist
        self.assertIsNotNone(self.app.main_content)
        self.assertIsNotNone(self.app.sidebar)

    def test_macos_configuration(self):
        """Test macOS-specific settings."""
        # You can skip this or mock it if needed
        if sys.platform == "darwin":
            with self.assertLogs(level="INFO") as log:
                self.app._configure_macos_settings()
                self.assertIn("pyobjc library is missing.", log.output[0] or "MacOS configuration error:")

    def test_create_menu(self):
        """Test the creation of the menu."""
        # Check if 'File' menu is created
        menubar = self.root.config('menu')[-1]
        file_menu = menubar.index('file')
        self.assertIsNotNone(file_menu)

    def test_navigation(self):
        """Test navigation to different pages."""
        # Mock the page creation functions
        self.app.show_page = MagicMock()

        # Test navigation to 'flights' page
        self.app.handle_navigation("flights")
        self.app.show_page.assert_called_with("flights")

        # Test navigation to 'clients' page
        self.app.handle_navigation("clients")
        self.app.show_page.assert_called_with("clients")

    def test_restart_app(self):
        """Test the restart app functionality."""
        with self.assertRaises(SystemExit):  # Restart will raise a SystemExit error
            self.app.restart_app()

    def test_show_page(self):
        """Test showing different pages."""
        # Mocking page components
        self.app.show_page("flights")
        self.assertEqual(self.app.current_page.__class__, MagicMock)

        self.app.show_page("clients")
        self.assertEqual(self.app.current_page.__class__, MagicMock)

    def tearDown(self):
        """Clean up after each test."""
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
