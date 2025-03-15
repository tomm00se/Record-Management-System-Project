"""
Reusable Sidebar Module that can be reused across different pages
of the Record Management System
"""

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

class Sidebar:
    """
    Reusable sidebar component for navigation.
    """

    def __init__(self, parent, active_btn="Flights"):
        """
        Initialize sidebar with navigation buttons.
        
        Args:
            parent: Parent widget
            active_btn (str): Currently active button name
        """
        self.parent = parent
        self.active_btn = active_btn
        self.create_sidebar()

    def create_sidebar(self):
        """Create and configure the sidebar with navigation buttons."""
        self.sidebar = ctk.CTkFrame(
            self.parent,
            width=96,
            fg_color="#F6F6F6",
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y",
            padx=0,
            pady=0
        )
        # Prevent the sidebar from resizing
        self.sidebar.pack_propagate(False)

        # Load icons
        icon_flights = ctk.CTkImage(Image.open(
            "../assets/icon_flights.png"), size=(32, 32))
        icon_clients = ctk.CTkImage(Image.open(
            "../assets/icon_clients.png"), size=(32, 32))
        icon_airlines = ctk.CTkImage(Image.open(
            "../assets/icon_airlines.png"), size=(32, 32))

        # Create buttons
        self.flight_btn = SidebarButton(
            self.sidebar,
            "Flights",
            icon_flights,
            command=lambda: self.navigate_to("flights")
        )
        self.flight_btn.pack(pady=6, padx=8)

        self.clients_btn = SidebarButton(
            self.sidebar,
            "Clients",
            icon_clients,
            command=lambda: self.navigate_to("clients")
        )
        self.clients_btn.pack(pady=6, padx=8)

        self.airlines_btn = SidebarButton(
            self.sidebar,
            "Airlines",
            icon_airlines,
            command=lambda: self.navigate_to("airlines")
        )
        self.airlines_btn.pack(pady=6, padx=8)

    def navigate_to(self, page):
        """
        Handle navigation between pages.
        
        Args:
            page (str): Page to navigate to
        """
        # Navigation logic will be implemented by the main app
        if hasattr(self, 'on_navigate'):
            self.on_navigate(page)
