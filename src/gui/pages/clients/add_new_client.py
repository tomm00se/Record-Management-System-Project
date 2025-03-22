"""New Client Form Module"""
import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.data.record_manager import RecordManager


class NewClientForm(BasePage):
    """New Client Form Class"""

    def __init__(self, parent, navigation_callback, record_manager: RecordManager):
        super().__init__(parent, navigation_callback)
        
        self.record_manager = record_manager

        # Create header
        self.create_header(
            "Add New Client",
            "Please enter the client information"
        )

        # Create form
        self.create_form()

    def create_form(self):
        """Create the form for adding a new client"""
        # Form container with scrollable frame
        # self.scroll_frame = ctk.CTkScrollableFrame(self.content_frame)
        # self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        form_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Client Name
        self.create_field(form_frame, "Name", True)
        self.name = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter Client name"
        )
        self.name.pack(fill="x", pady=(0, 15))

        # Address Section
        address_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        address_frame.pack(fill="x", pady=(0, 15))

        # Address Line 1 (with label)
        self.create_field(address_frame, "Address", True)
        self.address_line1 = ctk.CTkEntry(
            address_frame,
            placeholder_text="Address Line 1"
        )
        self.address_line1.pack(fill="x", pady=(0, 5))

        # Address Line 2 (no label)
        self.address_line2 = ctk.CTkEntry(
            address_frame,
            placeholder_text="Address Line 2"
        )
        self.address_line2.pack(fill="x", pady=(0, 5))

        # Address Line 3 (no label)
        self.address_line3 = ctk.CTkEntry(
            address_frame,
            placeholder_text="Address Line 3"
        )
        self.address_line3.pack(fill="x")

        # Location Frame (City, State, Zip Code)
        location_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        location_frame.pack(fill="x", pady=(0, 15))

        # City
        city_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        city_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.create_field(city_frame, "City", True)
        self.city = ctk.CTkEntry(
            city_frame,
            placeholder_text="Enter city"
        )
        self.city.pack(fill="x")

        # State
        state_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        state_frame.pack(side="left", fill="x", expand=True, padx=5)
        self.create_field(state_frame, "State", True)
        self.state = ctk.CTkEntry(
            state_frame,
            placeholder_text="Enter state"
        )
        self.state.pack(fill="x")

        # Zip Code
        zip_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        zip_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        self.create_field(zip_frame, "Zip Code", True)
        self.zip_code = ctk.CTkEntry(
            zip_frame,
            placeholder_text="Enter zip code"
        )
        self.zip_code.pack(fill="x")

        # Country
        self.create_field(form_frame, "Country", True)
        self.country = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter country"
        )
        self.country.pack(fill="x", pady=(0, 15))

        # Contact Frame (Phone and Email)
        contact_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        contact_frame.pack(fill="x", pady=(0, 15))

        # Phone
        phone_frame = ctk.CTkFrame(contact_frame, fg_color="transparent")
        phone_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.create_field(phone_frame, "Phone", True)
        self.phone = ctk.CTkEntry(
            phone_frame,
            placeholder_text="Enter phone number"
        )
        self.phone.pack(fill="x")

        # Email
        email_frame = ctk.CTkFrame(contact_frame, fg_color="transparent")
        email_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        self.create_field(email_frame, "Email", True)
        self.email = ctk.CTkEntry(
            email_frame,
            placeholder_text="Enter email address"
        )
        self.email.pack(fill="x")

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
        new_client = {
            "type": "Client",
            "name": self.name.get(),
            "address_line1": self.address_line1.get(),
            "address_line2": self.address_line2.get(),
            "address_line3": self.address_line3.get(),
            "city": self.city.get(),
            "state": self.state.get(),
            "zip_code": self.zip_code.get(),
            "country": self.country.get(),
            "phone": self.phone.get(),
            "email": self.email.get()
        }

        # Save client data to record manager
        self.record_manager.add_record("client", new_client)

        # Navigate back to clients page
        self.navigation_callback("clients")
