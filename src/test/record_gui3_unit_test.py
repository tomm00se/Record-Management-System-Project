""" 
Unit tests for record_gui3.py module
"""
import sys
import os
from os.path import dirname, abspath, join
import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
import customtkinter as ctk

# Add the project root directory to Python path
project_root = abspath(join(dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.gui.record_gui3 import RecordMgmtSystem


class TestRecordMgmtSystem(unittest.TestCase):
    """Test Cases for Record Management System"""

    def setUp(self):
        """Setup the Testing Environment"""
        self.root = ctk.CTk()
        self.root.geometry("1280x768")

        # Patches
        self.patches = [
            patch('src.gui.record_gui3.RecordManager'),
            patch('src.gui.pages.flights.flights.FlightsPage'),
            patch('src.gui.pages.clients.clients.ClientsPage'),
            patch('src.gui.pages.airlines.AirlinesPage')
        ]

        # Start all patches
        for p in self.patches:
            p.start()

        self.app = RecordMgmtSystem(self.root)
        self.root.update()

    def test_initialization(self):
        """Application Initialization Test"""
        # Get current geometry without position info
        current_geometry = self.root.geometry().split('+')[0]

        self.assertEqual(self.root.title(), "Record Management System")
        self.assertEqual(current_geometry, "1280x768")

        # Test if main components exist
        self.assertIsNotNone(self.app.main_content)
        self.assertIsNotNone(self.app.sidebar)
        self.assertIsNotNone(self.app.record_manager)
        self.assertIsNotNone(self.app.current_page)

    def test_platform_configuration(self):
        """Test Platform-Specific Settings"""
        with patch('src.gui.record_gui3.sys.platform') as mock_platform:
            # Test Windows configuration
            mock_platform.return_value = 'win32'
            self.app._configure_platform_settings()

            # Test macOS configuration
            mock_platform.return_value = 'darwin'
            self.app._configure_platform_settings()

    def test_create_menu(self):
        """Menu Creation Test"""
        with patch('tkinter.Menu') as mock_menu:
            mock_file_menu = MagicMock()
            mock_menu.return_value = mock_file_menu

            self.app.create_menu()

            mock_menu.assert_called()
            self.assertTrue(mock_file_menu.add_command.called)

    def test_navigation(self):
        """Navigation Test"""
        self.app.show_page = MagicMock()

        test_pages = ['flights', 'clients', 'airlines']
        for page in test_pages:
            self.app.handle_navigation(page)
            self.app.show_page.assert_called_with(page)

    def test_restart_app(self):
        """Restart Application Test"""
        with patch('os.execl') as mock_execl:
            with patch('sys.executable', 'python'):
                self.app.restart_app()
                mock_execl.assert_called()

    def test_show_page(self):
        """Page Display Test"""
        # Test pages with mocked classes
        test_pages = ['flights', 'clients', 'airlines']
        for page in test_pages:
            self.app.show_page(page)
            # Verify that a page was created
            self.assertIsNotNone(self.app.current_page)

    def tearDown(self):
        """Clean Up after each test"""
        # Stop all patches
        for p in self.patches:
            p.stop()

        try:
            self.root.destroy()
        except tk.TclError:
            pass


if __name__ == "__main__":
    unittest.main()
