""" Edit Client Page Module """
from tkinter import messagebox
import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.gui.components.select_fields import SelectCountry
from src.gui.components.headers import FormHeader
from src.gui.components.buttons import FormButtons, DeleteButton
from src.gui.components.form import FormComponents
from src.data.record_manager import RecordManager


class EditClientPage(BasePage):
    """Edit Client Page Class"""

    def __init__(self, parent, navigation_callback, record_manager: RecordManager, client_data=None):
        super().__init__(parent, navigation_callback)
        self.record_manager = record_manager
        self.form_components = FormComponents()
        
        self.client_data = client_data

        # Create Header
        self.header = FormHeader(
            self.content_frame,
            title="Edit Client",
            description="Please update the client information"
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
        """Create form for adding a new client"""
        # Client Frame
        client_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        client_frame.pack(fill="x", pady=(0, 0))

        # Client Name
        client_name_frame = ctk.CTkFrame(client_frame, fg_color="transparent")
        client_name_frame.pack(side="left", fill="x",
                               expand=True, padx=(0, 10))
        self.client = self.form_components.create_form_row(
            client_name_frame,
            "Client",
            required=True,
            field_type="text",
            placeholder="Enter Client name"
        )
        self.client.pack(fill="x", pady=(0, 0))
        self.client.insert(0, self.client_data["name"])
        
        # Phone
        phone_frame = ctk.CTkFrame(client_frame, fg_color="transparent")
        phone_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.phone = self.form_components.create_form_row(
            phone_frame,
            "Phone",
            required=True,
            field_type="text",
            placeholder="Enter Phone Number"
        )
        self.phone.pack(fill="x")
        self.phone.insert(0, self.client_data["phone"])

        # Email
        email_frame = ctk.CTkFrame(client_frame, fg_color="transparent")
        email_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        self.email = self.form_components.create_form_row(
            email_frame,
            "Email",
            required=True,
            field_type="text",
            placeholder="Enter Email Address"
        )
        self.email.pack(fill="x")
        self.email.insert(0, self.client_data["email"])

        # Address Section
        address_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        # Added bottom padding to section
        address_frame.pack(fill="x", pady=(0, 10))

        # Address Line 1 (with label)
        address_line1_frame = ctk.CTkFrame(
            address_frame, fg_color="transparent")
        address_line1_frame.pack(fill="x")
        # Create label and field separately for address line 1
        label = self.form_components.create_field_label(
            address_line1_frame, "Address", required=True)
        label.pack(anchor="w", pady=(0, 5))
        self.address_line1 = self.form_components.create_text_input(
            address_line1_frame,
            placeholder="Address Line 1"
        )
        self.address_line1.pack(fill="x", pady=(0, 8))
        self.address_line1.insert(0, self.client_data["address_line1"])

        # Address Line 2 (no label)
        address_line2_frame = ctk.CTkFrame(
            address_frame, fg_color="transparent")
        address_line2_frame.pack(fill="x")
        self.address_line2 = self.form_components.create_text_input(
            address_line2_frame,
            placeholder="Address Line 2"
        )
        self.address_line2.pack(fill="x", pady=(0, 8))
        self.address_line2.insert(0, self.client_data["address_line2"])

        # Address Line 3 (no label)
        address_line3_frame = ctk.CTkFrame(
            address_frame, fg_color="transparent")
        address_line3_frame.pack(fill="x")
        self.address_line3 = self.form_components.create_text_input(
            address_line3_frame,
            placeholder="Address Line 3"
        )
        self.address_line3.pack(fill="x", pady=(0, 8))
        self.address_line3.insert(0, self.client_data["address_line3"])

        # Location Frame (City, State, Zip Code)
        location_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        location_frame.pack(fill="x", pady=(0, 10))

        # City
        city_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        city_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.city = self.form_components.create_form_row(
            city_frame,
            "City",
            required=True,
            field_type="text",
            placeholder="Enter City"
        )
        self.city.pack(fill="x")
        self.city.insert(0, self.client_data["city"])

        # State
        state_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        state_frame.pack(side="left", fill="x", expand=True, padx=5)
        self.state = self.form_components.create_form_row(
            state_frame,
            "State",
            required=False,
            field_type="text",
            placeholder="Enter State"
        )
        self.state.pack(fill="x")
        self.state.insert(0, self.client_data["state"])

        # Zip Code
        zip_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        zip_frame.pack(side="left", fill="x", expand=True, padx=5)
        self.zip_code = self.form_components.create_form_row(
            zip_frame,
            "Zip",
            required=False,
            field_type="text",
            placeholder="Enter Zip Code"
        )
        self.zip_code.pack(fill="x")
        self.zip_code.insert(0, self.client_data["zip_code"])

        # Country
        country_frame = ctk.CTkFrame(location_frame, fg_color="transparent")
        country_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        # Create country selection
        self.country = self.form_components.create_form_row(
            country_frame,
            "Country",
            required=True,
            field_type="option",
            values=SelectCountry.COUNTRIES,
        )
        self.country.set("Please Select")  # Set default text
        self.country.set(self.client_data["country"])

        # Action Buttons
        self.action_buttons = FormButtons(
            self.form_container,
            cancel_command=self.on_cancel,
            save_command=self.on_save,
        )
        self.action_buttons.pack(fill="x", pady=(10, 0))

    def create_field(self, parent, label, required=False):
        """Create form field label"""
        label_text = f"{label} {'*' if required else ''}"
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Arial", 13)
        ).pack(anchor="w", pady=(0, 5))
        
    def validate_required_fields(self) -> tuple[bool, str]:
        """Validate all required fields are filled"""
        if not self.client.get():
            return False, "Please enter the client name"

        if not self.phone.get():
            return False, "Please enter the phone number"

        if not self.email.get():
            return False, "Please enter the email"

        if not self.address_line1.get():
            return False, "Please enter your address"

        if not self.city.get():
            return False, "Please enter city"

        if not self.country.get():
            return False, "Please enter country"

        return True, ""

    def on_cancel(self):
        """Handle cancel button click"""
        self.navigation_callback("clients")

    def on_save(self):
        """Handle save button click"""
        is_valid, error_message = self.validate_required_fields()
        if not is_valid:
            messagebox.showerror("Required Fields", error_message)
            return
        
        new_client = {
            "id": self.client_data["id"],
            "type": "Client",
            "name": self.client.get(),
            "phone": self.phone.get(),
            "email": self.email.get(),
            "address_line1": self.address_line1.get(),
            "address_line2": self.address_line2.get(),
            "address_line3": self.address_line3.get(),
            "city": self.city.get(),
            "state": self.state.get(),
            "zip_code": self.zip_code.get(),
            "country": self.country.get(),
            "created_at": self.client_data["created_at"]
        }

        self.record_manager.update_record("client", new_client["id"], new_client)

        self.navigation_callback("clients")
        
    def on_delete(self):
        """Handle delete button click"""
        self.record_manager.delete_record("client", self.client_data["id"])
        
        self.navigation_callback("clients")
