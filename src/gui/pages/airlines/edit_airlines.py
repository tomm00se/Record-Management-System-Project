""" Edit Airline Page Module """
from tkinter import messagebox
import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.gui.components.select_fields import SelectCountry
from src.gui.components.headers import FormHeader
from src.gui.components.buttons import FormButtons, DeleteButton
from src.gui.components.form import FormComponents
from src.data.record_manager import RecordManager


class EditAirlinePage(BasePage):
    """Edit Airline Page Class"""

    def __init__(self, parent, navigation_callback, record_manager: RecordManager, airline_data=None):
        super().__init__(parent, navigation_callback)
        self.record_manager = record_manager
        self.form_components = FormComponents()
        
        self.airline_data = airline_data

        # Create Header
        self.header = FormHeader(
            self.content_frame,
            title="Edit Airline",
            description="Please update the airline information"
        )
        self.header.pack(fill="x", padx=20, pady=(20, 0))

        # Create Delete Button Container
        self.delete_container = ctk.CTkFrame(
            self.content_frame, fg_color="transparent")
        self.delete_container.pack(fill="x", padx=20, pady=0)
        # Delete Flight Button
        self.delete_button = DeleteButton(
            self.delete_container,
            delete_command=self.on_delete,
            confirm_message="Are you sure you want to delete this record?"
        )
        
        # Form container
        self.form_container = ctk.CTkFrame(
            self.content_frame, fg_color="transparent")
        self.form_container.pack(fill="x", padx=20, pady=0)

        # Create form
        self.create_form()

    def create_form(self):
        """Create form for adding a new airline"""
        # Airline Frame
        airline_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        airline_frame.pack(fill="x", pady=(0, 0))

        # Airline Name
        self.company_name = self.form_components.create_form_row(
            airline_frame,
            "Airline",
            required=True,
            field_type="text",
            placeholder="Enter Airline Company Name"
        )
        self.company_name.pack(fill="x", pady=(0, 0))
        self.company_name.insert(0, self.airline_data["company_name"])

        # Country Frame
        country_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        country_frame.pack(fill="x", pady=(0, 0))

        # Country
        self.country = self.form_components.create_form_row(
            country_frame,
            "Country",
            required=True,
            field_type="option",
            values=SelectCountry.COUNTRIES,
        )
        self.country.pack(fill="x", pady=(0, 15))
        self.country.set(self.airline_data["country"])

        # Action Buttons
        self.action_buttons = FormButtons(
            self.form_container,
            cancel_command=self.on_cancel,
            save_command=self.on_save,
        )
        self.action_buttons.pack(fill="x", pady=(10, 0))

    def validate_required_fields(self) -> tuple[bool, str]:
        """Validate all required fields are filled"""
        if not self.company_name.get():
            return False, "Please enter the airline company"

        if self.country.get() == "Please Select":
            return False, "Please select country"

        return True, ""

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
        is_valid, error_message = self.validate_required_fields()
        if not is_valid:
            messagebox.showerror("Required Fields", error_message)
            return

        new_airline = {
            "id": self.airline_data["id"],
            "type": "Airline",
            "company_name": self.company_name.get(),
            "country": self.country.get(),
            "created_at": self.airline_data["created_at"]
        }
        
        self.record_manager.update_record(
            "airline", new_airline["id"], new_airline)

        self.navigation_callback("airlines")
        
    def on_delete(self):
        """Handle delete button click"""
        self.record_manager.delete_record("airline", self.airline_data["id"])
        
        self.navigation_callback("airlines")
