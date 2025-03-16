"""New Client Form Module"""
import customtkinter as ctk
from ..base import BasePage

class NewClientForm(BasePage):
    """New Client Form Class"""

    def __init__(self, parent, navigation_callback):
        super().__init__(parent, navigation_callback)

        # Create header
        self.create_header(
            "Add New Client",
            "Please enter the client information"
        )

        # Create form
        self.create_form()

    def create_form(self):
        """Create the form for adding a new client"""
        # Form container
        form_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        form_frame.pack(fill="both", expand=True)

        # Client Selection
        self.create_field(form_frame, "Client", True)
        self.client = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter client name"  # This shows helper text when empty
        )
        self.client.pack(fill="x", pady=(0, 15))

        # Airline Selection
        self.create_field(form_frame, "Airline", True)
        self.airline = ctk.CTkOptionMenu(
            form_frame,
            values=["Cathay Pacific Airways"]
        )
        self.airline.pack(fill="x", pady=(0, 15))

        # Cities Frame
        cities_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        cities_frame.pack(fill="x", pady=(0, 15))


        # Buttons
        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(20, 0))

        # Cancel Button
        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.on_cancel,
            fg_color="#E5E5EA",
            text_color="#000000"
        ).pack(side="left", padx=(0, 10))

        # Save Button
        ctk.CTkButton(
            button_frame,
            text="Save",
            command=self.on_save
        ).pack(side="left")

    def create_field(self, parent, label, required=False):
        """Create form field label"""
        label_text = f"{label} {'*' if required else ''}"
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Arial", 13)
        ).pack(anchor="w", pady=(0, 5))

    def on_cancel(self):
        """Handle cancel button click"""
        self.navigation_callback("clients")

    def on_save(self):
        """Handle save button click"""
        # Add validation and save logic
        self.navigation_callback("clients")
