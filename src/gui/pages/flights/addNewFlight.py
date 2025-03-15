"""
New Flight Form Module

This module implements the form for adding new flight records.
"""
import sys
import os
import customtkinter as ctk
from datetime import datetime
from components.sidebar import Sidebar

class NewFlightForm:
    """
    Form for creating new flight records.
    """

    def __init__(self, root, callback=None):
        """
        Initialize the new flight form.
        
        Args:
            root: Main window
            callback: Function to call after form submission
        """
        self.root = root
        self.callback = callback
        self.setup_form()

    def setup_form(self):
        """Create and configure the form layout."""
        # Add sidebar
        self.sidebar = Sidebar(self.root, active_btn="Flights")

        # Main content frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side="right", fill="both",
                             expand=True, padx=20, pady=20)

        # Header
        self.create_header()

        # Form fields
        self.create_form_fields()

        # Buttons
        self.create_buttons()

    def create_header(self):
        """Create form header with title and description."""
        title = ctk.CTkLabel(
            self.main_frame,
            text="Add New Flight",
            font=("Arial", 24, "bold")
        )
        title.pack(anchor="w", pady=(0, 10))

        description = ctk.CTkLabel(
            self.main_frame,
            text="Please select the client and enter the travel details to create the flight record",
            font=("Arial", 13)
        )
        description.pack(anchor="w", pady=(0, 20))

    def create_form_fields(self):
        """Create and configure form input fields."""
        # Client Selection
        self.create_field("Client", required=True)
        self.client_dropdown = ctk.CTkOptionMenu(
            self.main_frame,
            values=["0001 Leona Wong\nw.wong12@liverpool.ac.uk"]
        )
        self.client_dropdown.pack(fill="x", pady=(0, 15))

        # Airlines Selection
        self.create_field("Airlines", required=True)
        self.airline_dropdown = ctk.CTkOptionMenu(
            self.main_frame,
            values=["Cathay Pacific Airways"]
        )
        self.airline_dropdown.pack(fill="x", pady=(0, 15))

        # Create a frame for ticket type and cities
        details_frame = ctk.CTkFrame(self.main_frame)
        details_frame.pack(fill="x", pady=(0, 15))

        # Ticket Type
        type_frame = ctk.CTkFrame(details_frame)
        type_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.create_field("Ticket Type", required=True, parent=type_frame)
        self.ticket_type = ctk.CTkOptionMenu(
            type_frame,
            values=["One-Way", "Return"]
        )
        self.ticket_type.pack(fill="x")

        # Cities
        cities_frame = ctk.CTkFrame(details_frame)
        cities_frame.pack(side="left", fill="x", expand=True, padx=10)
        self.create_field("Start City", required=True, parent=cities_frame)
        self.start_city = ctk.CTkOptionMenu(
            cities_frame,
            values=["Hong Kong"]
        )
        self.start_city.pack(fill="x")

        end_city_frame = ctk.CTkFrame(details_frame)
        end_city_frame.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.create_field("End City", required=True, parent=end_city_frame)
        self.end_city = ctk.CTkOptionMenu(
            end_city_frame,
            values=["London"]
        )
        self.end_city.pack(fill="x")

        # Dates
        dates_frame = ctk.CTkFrame(self.main_frame)
        dates_frame.pack(fill="x", pady=(0, 15))

        # Depart Date
        depart_frame = ctk.CTkFrame(dates_frame)
        depart_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.create_field("Depart", required=True, parent=depart_frame)
        self.depart_date = ctk.CTkEntry(
            depart_frame,
            placeholder_text="Select date"
        )
        self.depart_date.pack(fill="x")

        # Return Date
        return_frame = ctk.CTkFrame(dates_frame)
        return_frame.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.create_field("Return", parent=return_frame)
        self.return_date = ctk.CTkEntry(
            return_frame,
            placeholder_text="Select date"
        )
        self.return_date.pack(fill="x")

    def create_buttons(self):
        """Create form submission buttons."""
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(fill="x", pady=(20, 0))

        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.cancel,
            fg_color="#E5E5EA",
            text_color="#000000"
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Save",
            command=self.save
        ).pack(side="left")

    def create_field(self, label, required=False, parent=None):
        """
        Create a form field label.
        
        Args:
            label (str): Field label text
            required (bool): Whether field is required
            parent: Parent widget for the label
        """
        if parent is None:
            parent = self.main_frame

        label_text = f"{label} {'*' if required else ''}"
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Helvetica", 13)
        ).pack(anchor="w")

    def cancel(self):
        """Handle form cancellation."""
        if self.callback:
            self.callback("cancel")

    def save(self):
        """Handle form submission."""
        # Implement save logic here
        if self.callback:
            self.callback("save")

    def run(self):
        """
        Start the application's main event loop.
    
        This method initiates the GUI application and handles all user interactions
        until the application is closed.
        """
        self.root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()  # Create the root window
    root.title("Add New Flight")
    root.geometry("1280x768")

    # Set appearance mode and color theme
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = NewFlightForm(root=root)  # Pass the root window
    app.run()
