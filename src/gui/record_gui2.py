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

Created Date: 15 March 2025
"""
import sys
import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image


class SidebarButton(ctk.CTkButton):
    """
    Sidebar button widget for sidebar navigation.

    This class extends CTkButton to create specialized buttons for the sidebar
    with specific styling and hover effects.
    """
    def __init__(self, btnSideBar, text, icon, **kwargs):
        """
        Initialize the sidebar button with custom styling.

        Args:
            btnSideBar: Parent widget container
            text (str): Button label text
            icon (CTkImage): Button icon image
            **kwargs: Additional keyword arguments for CTkButton
        """
        super().__init__(
            btnSideBar,
            text=text,
            image=icon,
            compound="top",
            width=54,  # Fixed width
            height=54,  # Fixed height
            fg_color="transparent",  # No background
            hover_color="#efefef",   # Light Grey background on hover
            border_width=0,          # No Border
            corner_radius=6,         # Rounded corners
            font=("Arial", 13, "normal"),  # Default font style
            text_color="#444444",    # Default text color
            anchor="center",  # Align Content to Center
            **kwargs  # This passes any additional arguments to CTkButton
        )

    # Bind hover events for cursor changes
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        """Change cursor to pointing hand on hover"""
        self.configure(cursor="pointinghand")

    def on_leave(self, event):
        """Restore default cursor when mouse leaves"""
        self.configure(cursor="arrow")

class RecordManagementSystem:
    """
    Main application class for the Record Management System.

    This class handles the creation and management of the main GUI components
    including the sidebar, main content area, and data displays.
    """
    def __init__(self):
        """Initialize the main application window and setup GUI components."""
        self.root = ctk.CTk()
        self.root.title("Record Management System")
        self.root.geometry("1280x768")
        
        # Configure macOS-specific settings
        self._configure_macos_settings()
            
        # Set application theme and color
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Initialize GUI components
        self.create_menu()
        self.create_sidebar()
        self.create_main_content()

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

    def create_sidebar(self):
        """
        Create and configure the application's sidebar navigation.
    
        reates a fixed-width sidebar containing navigation buttons for:
        - Flights
        - Clients
        - Airlines
    
        Each button includes an icon and label, with consistent styling and spacing.
        """
       # Configure Sidebar Container
        sidebar = ctk.CTkFrame(
            self.root,
            width=96,  # Set width to 96px
            fg_color="#F6F6F6",  # Set background color
            corner_radius=0  # Optional: removes rounded corners if you want
        )

        sidebar.pack(
            side="left",
            fill="y",
            padx=0,
            pady=0
        )

        # Prevent Sidebar from Resizing
        sidebar.pack_propagate(False)

        # Load Button Icons Images
        icon_flights = ctk.CTkImage(Image.open(
            "../assets/icon_flights.png"), size=(32, 32))
        icon_clients = ctk.CTkImage(Image.open(
            "../assets/icon_clients.png"), size=(32, 32))
        icon_airlines = ctk.CTkImage(Image.open(
            "../assets/icon_airlines.png"), size=(32, 32))

        # Create and pack navigation buttons
        flight_btn = SidebarButton(sidebar, "Flights", icon_flights)
        flight_btn.pack(pady=6, padx=8)

        clients_btn = SidebarButton(sidebar, "Clients", icon_clients)
        clients_btn.pack(pady=6, padx=8)

        airlines_btn = SidebarButton(sidebar, "Airlines", icon_airlines)
        airlines_btn.pack(pady=6, padx=8)

    def create_main_content(self):
        """
        Create and configure the main content area of the application.
    
        Creates a frame containing:
         - Header with title and action buttons
         - Table for displaying records
         - Pagination
        """
        # Main Content Container
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Header
        header_frame = ctk.CTkFrame(main_frame)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        # Header Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Flights",
            font=("Arial", 24, "bold")
        )
        title_label.pack(side="left")
        
        # Page Description
        # page_description = ctk.CTkLabel(
        #     header_frame,
        #     text="Create, edit, or manage client travel details for smooth trip planning"
        # )
        # page_description.pack(side="left", padx=20)

        # Add New Flight Button
        new_flight_btn = ctk.CTkButton(
            header_frame,
            text="+ New Flights")
        new_flight_btn.pack(side="right")

        # Table
        self.create_flight_table(main_frame)

        # Pagination
        self.create_pagination(main_frame)

    def create_flight_table(self, parent):
        """
        Create Flight Records Table
        """
        # Table Columns
        columns = ("ID", "Client", "Airline", "From", "To",
                   "Depart On", "Created On", "Action")
       
        # Initialize and configure Treeview
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")

        # Configure column headings and widths
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Add sample data for demonstration
        sample_data = [
            ("0001", "Leona Wong", "Cathay Pacific Airways", "Hong Kong",
             "London", "10 Apr 2025", "09 Mar 2025 18:38"),
            ("0002", "Leona Wong", "Cathay Pacific Airways", "London",
             "Hong Kong", "30 Apr 2025", "09 Mar 2025 18:38"),
        ]

        for item in sample_data:
            self.tree.insert("", "end", values=item)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(parent, 
                                  orient="vertical",
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack components
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

    def create_pagination(self, parent):
        """
        Create and configure pagination controls.
        """
        pagination_frame = ctk.CTkFrame(parent)
        pagination_frame.pack(fill="x", padx=10, pady=10)

        # Prev Button
        prev_btn = ctk.CTkButton(pagination_frame, text="Prev")
        prev_btn.pack(side="left")

        # Page numbers
        for i in range(1, 11):
            page_btn = ctk.CTkButton(
                pagination_frame,
                text=str(i),
                width=30
            )
            page_btn.pack(side="left", padx=2)
        
        # Next Button
        next_btn = ctk.CTkButton(pagination_frame, text="Next")
        next_btn.pack(side="right")

    def load_image(self, filename):
        """
        Load and return an image file.
        """
        return None

    def run(self):
        """
        Start the application's main event loop.
    
        This method initiates the GUI application and handles all user interactions
        until the application is closed.
        """
        self.root.mainloop()

if __name__ == "__main__":
    app = RecordManagementSystem()
    app.run()
