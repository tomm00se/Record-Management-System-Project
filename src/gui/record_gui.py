"""
Record Management System GUI

This module implements a graphical user interface for a Record Management System.
The application is built using CustomTkinter and consists of three main components:

1. Sidebar: Navigation panel with buttons for different sections
2. Search Bar: Interface for searching records
3. Main Frame: Display area for all content (e.g., tables, forms, etc.)

Classes:
    - SidebarButton: Custom button widget for sidebar navigation
    - RecordManagementSystem: Main application class handling the GUI layout

Version: 1.0

Created Date: 16 March 2025
"""
import sys
import os
from os.path import dirname, abspath, join
import tkinter as tk
import customtkinter as ctk
from src.gui.pages.flights import FlightsPage
from src.gui.pages.flights import NewFlightForm
from src.gui.pages.flights import EditFlightPage
from src.gui.pages.clients.clients import ClientsPage
from src.gui.pages.clients.add_new_client import NewClientForm
from src.gui.pages.clients.edit_clients import EditClientPage
from src.gui.pages.airlines import AirlinesPage
from src.gui.pages.airlines import NewAirlineForm
from src.gui.pages.airlines.edit_airlines import EditAirlinePage
from src.gui.components.sidebar import Sidebar
from src.data.record_manager import RecordManager

# Add the parent directory to the system path
sys.path.append(abspath(join(dirname(__file__), '..')))

class RecordMgmtSystem:
    """
    Main application class for the Record Management System.

    This class handles the creation and management of the main GUI components
    including the sidebar, main content area, and data displays.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Record Management System")
        self.root.geometry("1280x768")

        # Configure platform-specific settings
        self._configure_platform_settings()

        # Set application theme and color
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.record_manager = RecordManager(data_folder="src/record", file_format="json")
        
        # Initialize GUI components
        self.create_menu()

        # Create main content area
        self.main_content = ctk.CTkFrame(self.root)
        self.main_content.pack(side="right", fill="both", expand=True)
        
        # Initialize the sidebar with navigation callback
        self.sidebar = Sidebar(self.main_content, self.handle_navigation)
        self.sidebar.on_navigate = self.handle_navigation  # Set navigation callback

        # Show default page (Flights)
        self.current_page = None
        self.show_page("flights")

    def _configure_platform_settings(self):
        """Configure platform-specific settings for the application."""
        try:
            # Set application icon
            if sys.platform == "darwin":  # macOS
                # macOS specific settings
                try:
                    from Foundation import NSBundle
                    bundle = NSBundle.mainBundle()
                    info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
                    info['CFBundleName'] = "Record Management System"
                except ImportError:
                    pass

            # Set icon for both Windows and macOS
            try:
                icon_path = "src/assets/rms.png"
                if os.path.exists(icon_path):
                    icon = tk.PhotoImage(file=icon_path)
                    self.root.iconphoto(True, icon)
            except Exception as e:
                print(f"Icon loading error: {e}")

            # Windows specific settings
            if sys.platform == "win32":
                self.root.state('zoomed')  # Start maximized on Windows

        except Exception as e:
            print(f"Platform configuration error: {e}")


    def create_menu(self):
        """
        Create and configure the application's main menu bar.
    
        Creates a menu bar with 'File' menu containing options for:
        - Restart: Restarts the application
        - Exit: Closes the application
        """        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Restart", command=self.restart_app)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def restart_app(self):
        """
         Restart the application by re-executing the current process.

         This method terminates the current instance and starts a fresh instance
         of the application using the same arguments it was initially launched with.
        """
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def handle_navigation(self, page_name):
        """Handle navigation between pages"""
        self.show_page(page_name)

    def show_page(self, page_name):
        """Show the selected page"""
        # Clear current page if exists
        if self.current_page:
            self.current_page.destroy()
            
        record_data = None
        if isinstance(page_name, dict):
            record_data = page_name.get('data')
            page_name = page_name.get('route')

        # Show new page
        if page_name == "flights":
            self.current_page = FlightsPage(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "add_new_flight":
            self.current_page = NewFlightForm(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "edit_flight":
            self.current_page = EditFlightPage(
                self.main_content, self.handle_navigation, self.record_manager, record_data)
        elif page_name == "clients":
            self.current_page = ClientsPage(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "add_new_client":
            self.current_page = NewClientForm(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "edit_client":
            self.current_page = EditClientPage(
                self.main_content, self.handle_navigation, self.record_manager, record_data)
        elif page_name == "airlines":
            self.current_page = AirlinesPage(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "add_new_airline":
            self.current_page = NewAirlineForm(
                self.main_content, self.handle_navigation, self.record_manager)
        elif page_name == "edit_airline":
            self.current_page = EditAirlinePage(
                self.main_content, self.handle_navigation, self.record_manager, record_data)


        self.current_page.pack(fill="both", expand=True)

    def run(self):
        """
        Start the application's main event loop.
    
        This method initiates the GUI application and handles all user interactions
        until the application is closed.
        """
        self.root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = RecordMgmtSystem(root)
    root.mainloop()
