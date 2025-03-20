import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.data.record_manager import RecordManager


class EditAirlinePage(BasePage):
    """Edit Airline Update Form Class"""

    def __init__(self, parent, navigation_callback, record_manager: RecordManager, client_data=None):
        self.record_manager = record_manager
        
        super().__init__(parent, navigation_callback)
        
        self.client_data = client_data

        # Create header
        self.create_header(
            "Add New Client",
            "Please enter the client information"
        )

        # Create form
        self.create_form()

    def create_form(self):
        """Create form for adding a new airline"""
        # Form container
        form_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Airline Name
        self.create_field(form_frame, "Airline", True)
        self.name = ctk.CTkEntry(
            form_frame,
            fg_color="white",
            placeholder_text="Enter Airline Company Name"
        )
        self.name.pack(fill="x", pady=(0, 15))
        self.name.insert(0, self.client_data["company_name"])

        # Country
        self.create_field(form_frame, "Country", True)
        self.country = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter country"
        )
        self.country.pack(fill="x", pady=(0, 15))
        self.country.insert(0, self.client_data["country"])

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
        
        button_frame_delete = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame_delete.pack(fill="x", pady=(20, 0))

        # Delete Button
        ctk.CTkButton(
            button_frame_delete,
            text="Delete",
            command=self.on_delete,
            fg_color="#FF3B30",
            text_color="#FFFFFF"
        ).pack(side="left", padx=(0, 10))

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
        self.navigation_callback("airlines")

    def on_save(self):
        """Handle save button click"""
        
        new_airline = {
            "type": "Airline",
            "company_name": self.name.get(),
            "country": self.country.get()
        }
        
        self.record_manager.update_record("client", new_airline["id"], new_airline)

        self.navigation_callback("airlines")
        
    def on_delete(self):
        """Handle delete button click"""
        self.record_manager.delete_record("client", self.client_data["id"])
        
        self.navigation_callback("airlines")
