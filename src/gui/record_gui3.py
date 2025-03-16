"""
Main Container for Record Management System
"""
import sys
import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from pages.flights import FlightsPage
from pages.flights import NewFlightForm
from pages.flights import EditFlightPage
from pages.clients import ClientsPage
from pages.clients import NewClientForm
from pages.airlines import AirlinesPage
from pages.airlines import NewAirlineForm
from components.sidebar import Sidebar
# from .components.searchbar import SearchBar

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

        # Configure macOS-specific settings
        self._configure_macos_settings()

        # Set application theme and color
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
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

    def _configure_macos_settings(self):
        """Configure macOS settings for the application."""
        if sys.platform == "darwin":  # macOS
            try:
                from Foundation import NSBundle
                bundle = NSBundle.mainBundle()
                info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
                info['CFBundleName'] = "Record Management System"
                icon = tk.PhotoImage(file="../assets/rms.png")
                self.root.iconphoto(True, icon)
            except (ImportError, AttributeError) as e:
                print(f"MacOS configuration error: {e}")

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

        # Show new page
        if page_name == "flights":
            self.current_page = FlightsPage(
                self.main_content, self.handle_navigation)
        elif page_name == "add_new_flight":
            self.current_page = NewFlightForm(
                self.main_content, self.handle_navigation)
        elif page_name == "edit_flight":
            self.current_page = EditFlightPage(
                self.main_content, self.handle_navigation)
        elif page_name == "clients":
            self.current_page = ClientsPage(
                self.main_content, self.handle_navigation)
        elif page_name == "add_new_client":
            self.current_page = NewClientForm(
                self.main_content, self.handle_navigation)
        elif page_name == "airlines":
            self.current_page = AirlinesPage(
                self.main_content, self.handle_navigation)
        elif page_name == "add_new_airline":
            self.current_page = NewAirlineForm(
                self.main_content, self.handle_navigation)

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
    app.run()
